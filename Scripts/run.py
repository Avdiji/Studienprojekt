from Helper.wget import WGet

url_path = "../Domains/Chore_URLS.txt"
html_path = "../Domains/Domain_Mirror"
log_path = "../Domains/logfile.log"

wget = WGet(url_path, html_path, log_path)

# wget.mirror_domain()

wget.get_log_triple()
