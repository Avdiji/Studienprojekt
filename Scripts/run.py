from Helper.wget import *




single_domainList_path = "../Domain_List/Chore_URLS.txt"
single_logfile = "../Domain_List/single_logfile.log"
single_saveDirectory = "../Domain_List/Chore_HTML"


wget = WGet(single_domainList_path, single_saveDirectory)

# wget.download_html(single_logfile)
wget.download_html_sub('buchenbuehl','index.php/termine2020', single_logfile)