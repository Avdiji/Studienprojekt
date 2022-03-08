import spacy
import pandas
from spacy.matcher import Matcher
import json


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

    def load_all_patterns(self):
        result = []

        all_patterns = open(self.pattern_dataframe_path, 'r', encoding="UTF-8")
        for line in all_patterns:
            result.append(json.loads(line))
        all_patterns.close()

        return result

    def get_matcher(self):
        matcher = Matcher(self.nlp.vocab)
        all_patterns = [pattern for pattern in self.load_all_patterns()]
        matcher.add("", all_patterns)

        return matcher

    def create_csv(self):
        csv_dict = {"Choir-Name": [],
                    "Filtered Text": []}

        matcher = self.get_matcher()

        segmentation_df = pandas.read_csv(self.segmentation_dataframe_path)
        segmentation_df = segmentation_df.dropna()
        for elem in segmentation_df.iterrows():
            choir_name = elem[1][0]
            text = elem[1][3]

            print(text)
            print()
            doc = self.nlp(text)
            matching = get_matches_list(matcher, doc)
            if len(matching) > 0:
                csv_dict["Choir-Name"].append(choir_name)
                csv_dict["Filtered Text"].append(str(matching))

        new_dataframe = pandas.DataFrame(csv_dict, columns=["Choir-Name", "Filtered Text"]).drop_duplicates()
        new_dataframe.to_csv(self.nlp_dataframe_path, index=False)
