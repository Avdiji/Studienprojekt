from Helper.wget import WGet
from Helper.cleaning import Cleaning
from Helper.segmentation import Segmentation
from Helper.nlp import NLP

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

nlp = NLP(segmentation)




with open(url_path, "r") as f:
    for line in f:
        print(line.split(" ")[0], nlp.get_name_matcher(line.split(" ")[0]))
        # print(
        #     f"\t{segmentation.get_contacts_soup(line.split(' ')[0])}\n"
        # )
