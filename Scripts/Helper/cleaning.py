from bs4 import BeautifulSoup
import os


# ----------------------------------------------------------------------------------------------------
# parameter:
#       choir_name: name of the choir the appendix needs to be searched for
#
# Function returns the Appendix needed, to download the HTML-File with all the dates
# ----------------------------------------------------------------------------------------------------
def get_urlAppendix_dates(choir_name, dict_soup):
    result = dict_soup[choir_name + ".html"].find_all('a')

    if choir_name == "eibach":
        result = ""

    elif choir_name == "gebersdorf":
        result = [val for val in result if "Termine" in str(val)]
        result = str(result).split("\"")[1]

    elif choir_name == "gostenhof":
        result = [val for val in result if "wann-und-wo" in str(val)]
        result = str(result).split("\"")[3]

    elif choir_name == "grosreuth" or \
            choir_name == "heroldsberg" or \
            choir_name == "maxfeld" or \
            choir_name == "eibach":
        result = ""

    elif choir_name == "lichtenhof":
        result = [val for val in result if "Kirchenmusik" in str(val)]
        result = result[0]
        result = str(result).split("\"")[5]

    return result


# ----------------------------------------------------------------------------------------------------
# parameter:
#       choir_name: name of the choir the appendix needs to be searched for
#
# Function returns the Appendix needed, to download the HTML-File with all the contacts
# ----------------------------------------------------------------------------------------------------
def get_urlAppendix_contacts(choir_name, dict_soup):
    result = dict_soup[choir_name + ".html"].find_all('a')

    if choir_name == "eibach":
        result = [val for val in result if "Kontakt" in str(val)][0]
        result = str(result).split("\"")[3]

    elif choir_name == "gebersdorf":
        result = [val for val in result if "Kontakt" in str(val)][0]
        result = str(result).split("\"")[1]

    elif choir_name == "gostenhof":
        result = [val for val in result if "Kontakt" in str(val)][1]
        result = str(result).split("\"")[1]

    elif choir_name == "lichtenhof":
        result = [val for val in result if "Kirchenmusik" in str(val)]
        result = result[0]
        result = str(result).split("\"")[5]

    elif choir_name == "maxfeld" or choir_name == "grosreuth" or choir_name == "heroldsberg":
        result = ""

    return result


# ----------------------------------------------------------------------------------------------------
# Class is used to clean the downloaded html files, find and download subdomains
# and clean the html file from all scripts and stylesheets
# ----------------------------------------------------------------------------------------------------
class Cleaning:

    # ----------------------------------------------------------------------------------------------------
    #                               ***** CONSTRUCTOR *****
    # variables:
    #       wget: wget: object to be able to download HTML - Files
    #       html_path_dates: path to the path of the HTML - Files with the dates
    #       html_path_contacts: path to the path of the HTML - Files with the contacts
    #       dict_soup: Beautiful soup object to parse the HTML - Files
    #
    # ----------------------------------------------------------------------------------------------------
    def __init__(self, wget, html_path_dates, html_path_contacts):
        self.wget = wget
        self.html_path_dates = html_path_dates
        self.html_path_contacts = html_path_contacts
        self.dict_soup = {}

    # ----------------------------------------------------------------------------------------------------
    # Function acts as a setter for self.dict_soup (initializes dict_soup with the filenames(key) and the
    # corresponding BeautifulSoup4 Objects
    # ----------------------------------------------------------------------------------------------------
    def init_dict_soup(self):
        dir_list = os.listdir(self.wget.html_path)
        for filenames in dir_list:
            if os.path.isfile(f"{self.wget.html_path}/{filenames}"):
                bs = BeautifulSoup(open(f"{self.wget.html_path}/{filenames}", "rb"), "html.parser")
                self.dict_soup[filenames] = bs

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       choir_name: name of the choir
    #       log_path: path of the logfile
    #       info_type: type of the information (date or contact)
    #
    # returns:
    #       a BeautifulSoup4 object, that has been cleaned from the header, footer, css, and js
    #
    # Function returns a cleaned version of the HTML-File with the dates
    # ----------------------------------------------------------------------------------------------------
    def get_cleaned_soup(self, choir_name, info_type):

        if info_type == "date":
            self.wget.download_html_sub(choir_name, get_urlAppendix_dates(choir_name, self.dict_soup),
                                        self.html_path_dates)
            result = BeautifulSoup(open(f"{self.html_path_dates}/{choir_name}.html", "rb"), "html.parser")

        elif info_type == "contact":
            self.wget.download_html_sub(choir_name, get_urlAppendix_contacts(choir_name, self.dict_soup),
                                        self.html_path_contacts)
            result = BeautifulSoup(open(f"{self.html_path_contacts}/{choir_name}.html", "rb"), "html.parser")

        result = result.find("body")
        for deco in result(["script", "style", "head"]):
            deco.decompose()
        return result
