from Helper.wget import WGet
from Helper.cleaning_segmentation import CleaningSegmentation
from Helper.nlp_filter import NLP_Filter

url_path = "../Domains/Chore_URLS.txt"
html_path = "../Domains/Domain_Mirror"
log_path = "../Domains/logfile.log"

wget_dataframe_path = "../Dataframes/wget_dataframe.csv"
segmentation_dataframe_path = "../Dataframes/segmentation_dataframe.csv"
nlp_dataframe_path = "../Dataframes/nlp_dataframe.csv"
pattern_dataframe_path = "../Dataframes/patterns.csv"

wget = WGet(url_path, html_path, log_path, wget_dataframe_path)
print("Mirroring Websites...")
wget.mirror_domain()
wget.wget_create_csv()
print("Websites successfully Mirrored!")

print("Segmenting Websites...")
cl_seg = CleaningSegmentation(segmentation_dataframe_path, wget_dataframe_path)
cl_seg.execute_segmentation()
print("Websites Successfully Segmented!")

print("Filtering Segments...")
nlp = NLP_Filter(nlp_dataframe_path, pattern_dataframe_path, segmentation_dataframe_path)
nlp.create_csv()
print("Segments Successfully filtered!")
