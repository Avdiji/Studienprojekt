# ----------------------------------------------------------------------------------------------------
# Class is used to segment the cleaned HTML - Files into different
# categories (date, contact, location...)
# ----------------------------------------------------------------------------------------------------
class Segmentation:

    # ----------------------------------------------------------------------------------------------------
    #                               ***** CONSTRUCTOR *****
    # variables:
    #       clean: object to be able to clean the HTML - Files
    #
    # ----------------------------------------------------------------------------------------------------
    def __init__(self, clean):
        self.clean = clean

    # ----------------------------------------------------------------------------------------------------
    # parameters:
    #       choir_name: name of the choir
    #
    # Method filters the dates of the corresponding choir
    # ----------------------------------------------------------------------------------------------------
    def get_dates_soup(self, choir_name):
        result = self.clean.get_cleaned_soup(choir_name, "date")

        if choir_name == "eibach":
            result = result.find("table")

        elif choir_name == "gebersdorf" or choir_name == "gostenhof":
            result = result.find_all("p")[0]

        return result.getText()

    # ----------------------------------------------------------------------------------------------------
    # parameters:
    #       choir_name: name of the choir
    #
    # Method filters the contacts of the corresponding choir
    # ----------------------------------------------------------------------------------------------------
    def get_contacts_soup(self, choir_name):
        result = self.clean.get_cleaned_soup(choir_name, "contact")

        if choir_name == "eibach" or choir_name == "gebersdorf":
            result = result.find_all("p")[0]

        elif choir_name == "gostenhof":
            result = result.find_all("p")[2]

        return result.getText()
