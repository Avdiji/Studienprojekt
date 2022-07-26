import spacy
import pandas
from spacy.language import Language
import re


def retokenize(reg, ent_type, doc):
    for match in re.finditer(reg, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")

        if span is not None:
            with doc.retokenize() as retokenizer:
                attr = {"LEMMA": True,
                        "ENT_TYPE": ent_type}
                retokenizer.merge(span, attrs=attr)


@Language.component("markdownLinks_2_spans")
def rt_doc(doc):
    reg_time_eibach = r"\d\d.\d\d Uhr bis \d\d.\d\d Uhr"
    reg_time_maxfeld = r"\d\d.\d\d - \d\d.\d\d Uhr"
    reg_time_ziegelstein = r"\d\d.\d\d Uhr"
    reg_time_schniegling = r"\d\d:\d\d Uhr - \d\d:\d\d Uhr"
    reg_day = r"(m|M)ontag|(d|D)ienstag|(m|M)ittwoch|(d|D)onnerstag|(f|F)reitag|(s|S)amstag|(s|S)onntag"

    retokenize(reg_time_eibach, "TIME", doc)
    retokenize(reg_time_maxfeld, "TIME", doc)
    retokenize(reg_time_ziegelstein, "TIME", doc)
    retokenize(reg_time_schniegling, "TIME", doc)
    retokenize(reg_day, "DAY", doc)

    return doc


def create_filtered_text(doc):
    result = []
    valid_day = False
    valid_time = False

    for token in doc:
        if token.ent_type_ == "TIME" or token.ent_type_ == "DAY":
            if token.ent_type_ == "DAY":
                valid_day = True
            if token.ent_type_ == "TIME":
                valid_time = True
            result.append(str(token))

    return "".join(token + " " for token in result) if valid_time and valid_day else ""


class NLP_Filter:

    def __init__(self, nlp_dataframe_path, pattern_dataframe_path, segmentation_dataframe_path):
        self.nlp = spacy.load("de_core_news_sm")
        self.nlp_dataframe_path = nlp_dataframe_path
        self.pattern_dataframe_path = pattern_dataframe_path
        self.segmentation_dataframe_path = segmentation_dataframe_path

    def create_csv(self):
        self.nlp.add_pipe("markdownLinks_2_spans", name="markdownLinks_2_spans", first=True)
        csv_dict = {"Choir-Name": [],
                    "Filtered Text": [],
                    "Corresponding Paragraph": []}

        segmentation_df = pandas.read_csv(self.segmentation_dataframe_path)
        segmentation_df = segmentation_df.dropna()

        for elem in segmentation_df.iterrows():
            choir_name = elem[1][0]
            text = elem[1][3]

            doc = self.nlp(text)
            filtered = create_filtered_text(doc)

            print(text)

            if len(filtered) > 0:
                csv_dict["Choir-Name"].append(choir_name)
                csv_dict["Filtered Text"].append(filtered)
                csv_dict["Corresponding Paragraph"].append(text)

        new_dataframe = pandas.DataFrame(csv_dict, columns=["Choir-Name", "Filtered Text",
                                                            "Corresponding Paragraph"]).drop_duplicates()
        new_dataframe.to_csv(self.nlp_dataframe_path, index=False)
