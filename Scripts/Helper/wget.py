import os
import re


# TODO write logfile parser (choir, save path, filename), use pandas to save parser-returns in csv

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
    # all html files, found in the logfile (as a triple) in a list
    #
    # Return a list of triples, that each contain the information described above
    # ----------------------------------------------------------------------------------------------------
    def get_log_triple(self):
        result = []
        a = self.log_path
        tmp = "Wird in »../Domains/Domain_Mirror/eibach/posaunenchor-eibach.jimdofree.com/index.html".split("/")

        val1 = tmp[3]
        val3 = tmp[len(tmp) - 1]
        val2 = "".join(i + "/" for i in tmp[1:-1])

        result.append((val1, val2, val3))
        print(result)
        return result
