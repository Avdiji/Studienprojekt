import spacy
from spacy.matcher import Matcher


def get_matches_list(matcher, doc):
    result = []
    for match_id, start, end in matcher(doc):
        result.append(doc[start:end])
    return result


class NLP:
    def __init__(self, segmentation):
        self.nlp = spacy.load("de_core_news_lg")
        self.segmentation = segmentation

    def get_mail_matcher(self, choir_name):
        doc = self.nlp(self.segmentation.get_contacts_soup(choir_name))
        matcher = Matcher(self.nlp.vocab)
        pattern = [{"LIKE_EMAIL": True}]
        matcher.add(f"{choir_name}_mail", [pattern])

        return get_matches_list(matcher, doc)

    def get_name_matcher(self, choir_name):
        doc = self.nlp(self.segmentation.get_contacts_soup(choir_name))
        matcher = Matcher(self.nlp.vocab)
        pattern = [{"ENT_TYPE": "PER"}]
        matcher.add(f"{choir_name}_name", [pattern])

        return get_matches_list(matcher, doc)

    def get_tel_matcher(self, choir_name):
        doc = self.nlp(self.segmentation.get_contacts_soup(choir_name))
        matcher = Matcher(self.nlp.vocab)
        pattern = [{"LOWER": "telefon"}, {"LIKE_NUM": True}]
        matcher.add(f"{choir_name}_tel", [pattern])

        return get_matches_list(matcher, doc)

