import os
#TODO use proper wget command, write logfile parser (choir, save path, filename), use pandas to save parserreturns in csv, delete the bullshit

# ----------------------------------------------------------------------------------------------------
# Class Handles everything that evolves around downloading html files
# ----------------------------------------------------------------------------------------------------
class WGet:

    # ----------------------------------------------------------------------------------------------------
    #                               ***** CONSTRUCTOR *****
    # variables:
    #       url_path: path to the textfile, that contains all the urls
    #       html_path: path to the directory, where all the html files are supposed to be saved at
    #       url_dict: dictionary with the names of the choirs(key) and the corresponding urls(value)
    #
    # Constructor creates a dictionary with the names of the choirs(key) and the corresponding urls(value)
    # ----------------------------------------------------------------------------------------------------
    def __init__(self, url_path, html_path, log_path):

        self.url_dict = dict(
            [(url.split(' ')[0], url.split(' ')[1].replace('\n', ''))
             for url in open(url_path, 'r', encoding="UTF-8")])

        self.url_path = url_path
        self.html_path = html_path
        self.log_path = log_path

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       domains_path: path to the textfile with the website - URLs
    #       saving_destination: path to the saving destination of the corresponding html-files
    #       log_path: path to the saving destination of the corresponding logfile
    #
    # Function saves several websites as a html
    # ----------------------------------------------------------------------------------------------------
    def download_html(self):
        wget_createLog = f"wget -a {self.log_path}"

        if os.path.isfile(self.log_path): os.remove(self.log_path)
        for url_key, url_value in self.url_dict.items():
            os.system(wget_createLog + f" -O {self.html_path}/{url_key}.html -nc {url_value}")

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       choir_name : Name of the corresponding choir
    #       append_url: URL-Path which leads to the dates of the choir
    #       log_path: path to the saving destination of the corresponding logfile
    #       save_path: path to the saving destination of the html
    #
    # Function deletes the previous html file and downloads the one with all the information needed.
    # ----------------------------------------------------------------------------------------------------
    def download_html_sub(self, choir_name, append_url, save_path):
        saving_destination = f"{save_path}/{choir_name}.html"
        wget_createLog = f"wget -a {self.log_path} "

        os.system(wget_createLog + f"-O {saving_destination} -nc {self.url_dict[choir_name]}{append_url}")
