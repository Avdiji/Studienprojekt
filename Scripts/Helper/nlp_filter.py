import spacy
import pandas
from spacy.matcher import Matcher
from .nlp_patterns import patterns


def get_matches_list(matcher, doc):
    result = []
    for match_id, start, end in matcher(doc):
        result.append(doc[start:end])
    return result


class NLP_Filter:

    def __init__(self, nlp_dataframe_path, pattern_dataframe_path, segmentation_dataframe_path):
        self.nlp = spacy.load("de_core_news_lg")
        self.nlp_dataframe_path = nlp_dataframe_path
        self.pattern_dataframe_path = pattern_dataframe_path
        self.segmentation_dataframe_path = segmentation_dataframe_path

    def add_ruler(self):
        configuration = {"phrase_matcher_attr": "LEMMA"}

        ruler = self.nlp.add_pipe("entity_ruler", config=configuration)
        ruler.add_patterns(patterns)

        # text = "dienstags von 20.00 Uhr bis 21.30 Uhr"


        doc = self.nlp("Dienstags von 20:00 Uhr bis 21.30 Uhr")

        for ent in doc.ents:
            print(ent, ent.label_)


    # def get_matcher(self):
    #     matcher = Matcher(self.nlp.vocab)
    #     all_patterns = [pattern for pattern in self.load_all_patterns()]
    #     matcher.add("", all_patterns)
    #
    #     return matcher
    #
    #
    # def create_csv(self):
    #     csv_dict = {"Choir-Name": [],
    #                 "Filtered Text": []}
    #
    #     matcher = self.get_matcher()
    #
    #     segmentation_df = pandas.read_csv(self.segmentation_dataframe_path)
    #     segmentation_df = segmentation_df.dropna()
    #     for elem in segmentation_df.iterrows():
    #         choir_name = elem[1][0]
    #         text = elem[1][3]
    #
    #         print(text)
    #         print()
    #         doc = self.nlp(text)
    #         matching = get_matches_list(matcher, doc)
    #         if len(matching) > 0:
    #             csv_dict["Choir-Name"].append(choir_name)
    #             csv_dict["Filtered Text"].append(str(matching))
    #
    #     new_dataframe = pandas.DataFrame(csv_dict, columns=["Choir-Name", "Filtered Text"]).drop_duplicates()
    #     new_dataframe.to_csv(self.nlp_dataframe_path, index=False)
