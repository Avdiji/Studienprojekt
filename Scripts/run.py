from Helper.wget import WGet
from Helper.cleaning import Cleaning, get_urlAppendix_dates, get_urlAppendix_contacts
from Helper.segmentation import Segmentation

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

#segmentation.get_dates_soup("gostenhof")
#segmentation.get_dates_soup("eibach")
#segmentation.get_dates_soup("gebersdorf")

#segmentation.get_contacts_soup("eibach")
#segmentation.get_contacts_soup("gebersdorf")
#segmentation.get_contacts_soup("gostenhof")

clean.get_cleaned_soup("lichtenhof", "date")
