from Single_Domains.single_wget import download_html_single

single_domainList_path = "../Domain_List/Single_Domains.txt"
single_logfile = "../Domain_List/Single_Domains_HTML/single_logfile.log"
single_saveDirectory = "../Domain_List/Single_Domains_HTML"

download_html_single(single_domainList_path, single_saveDirectory, single_logfile)