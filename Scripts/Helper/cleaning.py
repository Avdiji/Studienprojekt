from bs4 import BeautifulSoup
import os


# ----------------------------------------------------------------------------------------------------
# Class is used to clean the downloaded html files, find and download subdomains
# and clean the html file from all scripts and stylesheets
# ----------------------------------------------------------------------------------------------------
class Cleaning:
    # ----------------------------------------------------------------------------------------------------
    #                               ***** CONSTRUCTOR *****
    # variables:
    #       wget: wget: object to be able to download HTML - Files
    #       dict_soup: Beautiful soup object to parse the HTML - Files
    #
    # Constructor initializes wget and dict_soup objects
    # ----------------------------------------------------------------------------------------------------
    def __init__(self, wget):
        self.wget = wget
        self.dict_soup = {}

    # ----------------------------------------------------------------------------------------------------
    # Function acts as a setter for self.dict_soup (initializes dict_soup with the filenames(key) and the
    # corresponding BeautifulSoup4 Objects
    # ----------------------------------------------------------------------------------------------------
    def init_dict_soup(self):
        dir_list = os.listdir(self.wget.html_path)
        for filenames in dir_list:
            bs = BeautifulSoup(open(f"{self.wget.html_path}/{filenames}", "rb"), "html.parser")
            self.dict_soup[filenames] = bs

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       choir_name: name of the choir the appendix needs to be searched for
    #
    # Function returns the Appendix needed, to download the HTML-File with all the dates
    # ----------------------------------------------------------------------------------------------------
    def get_urlAppendix(self, choir_name):
        result = ""

        if choir_name == "eibach":
            result = "/aktuelle-termine"
        elif choir_name == "gebersdorf":
            result = "/neues-termine"
        elif choir_name == "gostenhof":
            result = "/wann-und-wo-"
        elif choir_name == "grosreuth":
            result = ""
        return result

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       choir_name: name of the choir
    #       log_path: path of the logfile
    #
    # returns:
    #       a BeautifulSoup4 object, that has been cleaned from the header, footer, css, and js
    #
    # Function returns a cleaned version of the HTML-File with the dates
    # ----------------------------------------------------------------------------------------------------
    def get_cleaned_soup(self, choir_name, log_path):
        self.wget.download_html_sub(choir_name, self.get_urlAppendix(choir_name), log_path)
        self.dict_soup[choir_name] = BeautifulSoup(open(f"{self.wget.html_path}/{choir_name}.html", "rb"),
                                                   "html.parser")

        result = self.dict_soup[choir_name].find("body")
        for deco in result(["script", "style", "head", "footer"]):
            deco.decompose()
        return result
