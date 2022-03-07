from time import time
from Helper.wget import WGet
from Helper.cleaning_segmentation import CleaningSegmentation, clean_html, segment_html


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

wget_dataframes_path = "../Dataframes/wget_dataframe.csv"
segmentation_dataframes_path = "../Dataframes/segmentation_dataframe.csv"

wget = WGet(url_path, html_path, log_path, wget_dataframes_path)

wget.mirror_domain()
wget.wget_create_csv()

cl_seg = CleaningSegmentation(segmentation_dataframes_path, wget_dataframes_path)

cl_seg.execute_segmentation()
