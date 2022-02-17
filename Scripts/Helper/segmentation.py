class Segmentation:

    def __init__(self, clean):
        self.clean = clean

    def get_dates_soup(self, choir_name, log_path):
        result = self.clean.get_cleaned_soup(choir_name, log_path)

        if choir_name == "eibach":
            result = result.find("table")
        elif choir_name == "gebersdorf" or choir_name == "gostenhof":
            result = result.find_all("p")[0]
        elif choir_name == "grosreuth":
            result = result.find_all("p")[0]

        return result.getText()
