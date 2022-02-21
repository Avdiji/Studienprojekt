from Helper.wget import WGet
from Helper.cleaning import Cleaning
from Helper.segmentation import Segmentation
import os

url_path = "../Domain_List/Chore_URLS.txt"
log_path = "../Domain_List/single_logfile.log"

html_path = "../Domain_List/Chore_HTML"
html_path_dates = "../Domain_List/Chore_HTML/Chore_HTML_Dates"
html_path_contacts = "../Domain_List/Chore_HTML/Chore_HTML_Contacts"

wget = WGet(url_path, html_path, log_path)
wget.download_html()

clean = Cleaning(wget, html_path_dates, html_path_contacts)
clean.init_dict_soup()

segmentation = Segmentation(clean)

dir_list = os.listdir(html_path)
for filenames in dir_list:
    if os.path.isfile(f"{html_path}/{filenames}"):
        clean.get_cleaned_soup(filenames[:-5], "date")

dir_list = os.listdir(html_path)
for filenames in dir_list:
    if os.path.isfile(f"{html_path}/{filenames}"):
        clean.get_cleaned_soup(filenames[:-5], "contact")


#fix
