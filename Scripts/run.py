from Helper.wget import WGet
from Helper.cleaning import Cleaning

url_path = "../Domain_List/Chore_URLS.txt"
html_path = "../Domain_List/Chore_HTML"
log_path = "../Domain_List/single_logfile.log"


wget = WGet(url_path, html_path)
wget.download_html(log_path)

clean = Cleaning(wget)
clean.init_dict_soup()
clean.get_cleaned_soup("eibach", log_path)