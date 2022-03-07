import os
import re
import pandas
from datetime import datetime


def get_time():
    timer = datetime.now()
    return timer.strftime("%d/%m/%Y %H:%M:%S")


# ----------------------------------------------------------------------------------------------------
# Class Handles everything that evolves around downloading html files
# ----------------------------------------------------------------------------------------------------
class WGet:

    # ----------------------------------------------------------------------------------------------------
    #                                CONSTRUCTOR
    # variables:
    #       url_path: path to the textfile, that contains all the urls
    #       html_path: path to the directory, where all the html files are supposed to be saved at
    #       url_dict: dictionary with the names of the choirs(key) and the corresponding urls(value)
    #
    # Constructor creates a dictionary with the names of the choirs(key) and the corresponding urls(value)
    # ----------------------------------------------------------------------------------------------------
    def __init__(self, url_path, html_path, log_path, dataframes_path):

        self.url_dict = dict(
            [(url.split(' ')[0], url.split(' ')[1].replace('\n', ''))
             for url in open(url_path, 'r', encoding="UTF-8")])

        self.url_path = url_path
        self.html_path = html_path
        self.log_path = log_path
        self.dataframes_path = dataframes_path + "wget_dataframe.csv"

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #       domains_path: path to the textfile with the website - URLs
    #       saving_destination: path to the saving destination of the corresponding html-files
    #       log_path: path to the saving destination of the corresponding logfile
    #
    # Function saves several websites as a html
    # ----------------------------------------------------------------------------------------------------
    def mirror_domain(self):

        wget_createLog = f"wget -a {self.log_path} "
        wget_reject_datatypes = f"--reject JPG,jpg,png,mp3,pdf,MP4,mp4 "

        if os.path.isfile(self.log_path): os.remove(self.log_path)

        for url_key, url_value in self.url_dict.items():
            wget_save_in_path = f"-P {self.html_path}/{url_key} "
            wget_mirror = f"-N -c --mirror {url_value}"

            os.system(wget_createLog + wget_save_in_path + wget_reject_datatypes + wget_mirror)

    # ----------------------------------------------------------------------------------------------------
    # Method acts as a parser for the log_file. It saves the corresponding choir-name, path and name of
    # all html files, found in the logfile (as a dict)
    #
    # Return a dict, that each contain the information described above
    # ----------------------------------------------------------------------------------------------------
    def get_log_dict(self):

        result = {"Choirname": [],
                  "Path": [],
                  "Filename": [],
                  "Last Update": []}

        regex = 'Wird in ([^ ]*)(.html[^ ]*)'

        file = open(self.log_path, "r", encoding="UTF-8")
        lines = "".join([str(i) for i in file.readlines()])
        tmp = re.findall(regex, lines)

        for elem in tmp:
            val_all = (elem[0] + elem[1][:-1]).split('/')

            result["Choirname"].append(val_all[3])
            result["Path"].append("../" + "".join(i + "/" for i in val_all[1:-1]))
            result["Filename"].append(val_all[len(val_all) - 1])
            result["Last Update"].append(get_time())

        return result

    # ----------------------------------------------------------------------------------------------------
    # Method creates and saves a dataframe with all the needed information for cleaning and segmentation
    # ----------------------------------------------------------------------------------------------------
    def create_csv(self):
        new_dataframe = pandas.DataFrame(self.get_log_dict(), columns=["Choirname", "Path", "Filename", "Last Update"])
        existing_dataframe = pandas.read_csv(self.dataframes_path)

        merged_dataframe = pandas.concat([new_dataframe, existing_dataframe])
        merged_dataframe.drop_duplicates(subset=["Choirname", "Path", "Filename"], inplace=True)
        merged_dataframe.to_csv(self.dataframes_path, index=False)
