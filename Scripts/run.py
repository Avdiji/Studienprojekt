from Helper.wget import WGet

url_path = "../Domains/Chore_URLS.txt"
html_path = "../Domains/Domain_Mirror"
log_path = "../Domains/logfile.log"
dataframes_path = "../Dataframes/"

wget = WGet(url_path, html_path, log_path, dataframes_path)

# wget.mirror_domain()
wget.create_csv()
