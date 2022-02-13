import os


def download_html_single(domains_path, saving_destination, log_path):
    wget_createLog = f"wget -a {log_path} "

    if os.path.isfile(log_path): os.remove(log_path)

    urls = open(domains_path, 'r+', encoding="UTF-8")
    for url in urls:
        hlp = url.split('^')
        os.system(wget_createLog + f"-O {saving_destination}/{hlp[0]}.html -nc {hlp[1]}")
