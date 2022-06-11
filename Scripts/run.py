from time import time

from Helper.wget import WGet
from Helper.cleaning_segmentation import CleaningSegmentation
from Helper.nlp_filter import NLP_Filter


def performance(func):
    def wrapper_function(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2 - t1} seconds.")
        return result

    return wrapper_function


url_path = "../Domains/Chore_URLS.txt"
html_path = "../Domains/Domain_Mirror"
log_path = "../Domains/logfile.log"

wget_dataframe_path = "../Dataframes/wget_dataframe.csv"
segmentation_dataframe_path = "../Dataframes/segmentation_dataframe.csv"
nlp_dataframe_path = "../Dataframes/nlp_dataframe.csv"
pattern_dataframe_path = "../Dataframes/patterns.csv"

wget = WGet(url_path, html_path, log_path, wget_dataframe_path)

wget.mirror_domain()
wget.wget_create_csv()

cl_seg = CleaningSegmentation(segmentation_dataframe_path, wget_dataframe_path)

cl_seg.execute_segmentation()


nlp = NLP_Filter(nlp_dataframe_path, pattern_dataframe_path, segmentation_dataframe_path)

nlp.create_csv()


import re

# print(re.findall(reg, "Wir proben immer dienstags von 20.00 Uhr bis 21.30 im Gemeindezentrum. Ausbildung neuer Bläser jederzeit nach Absprache möglich."))
# print(re.findall(reg, "Probe jeden Montag, 19 Uhr, Gemeindehaus Stephanus,"))