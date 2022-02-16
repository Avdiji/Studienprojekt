from bs4 import BeautifulSoup
import os


def get_HTML_Dict(html_path):
    dict_result = {}

    dir_list = os.listdir(html_path)
    for filenames in dir_list:
        dict_result[filenames] = BeautifulSoup(open(f"{html_path}/{filenames}", "rb"), "html.parser")
    return dict_result