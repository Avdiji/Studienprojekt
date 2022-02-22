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
            result = result.find("footer")
            result = result.find_all("p")[0]

        elif choir_name == "gebersdorf" or choir_name == "gostenhof":
            result = result.find_all("p")[0]

        elif choir_name == "grosreuth":
            result = result.find_all(class_="et_tag")
            result = "".join(e.getText() for e in result)

        elif choir_name == "heroldsberg":
            result = result.find_all("p")[0]

        elif choir_name == "lichtenhof":
            result = result.find_all("p")[20]

        elif choir_name == "maxfeld":
            result = result.find_all(class_="Textkörper P-1")
            result = "".join(e.getText() for e in result)

        return result if isinstance(result, str) else result.getText()

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
            result = result.find(class_="bubble_box c3")
            result.find_all("p")

        elif choir_name == "grosreuth":
            result = result.find_all("p")[4]

        elif choir_name == "heroldsberg":
            result = result.find_all("p")[1]

        elif choir_name == "lichtenhof":
            result = result.find_all("p")[21]

        elif choir_name == "maxfeld":
            result = result.find_all(class_="Normal P-1")
            result = "".join(e.getText() for e in result)

        return result if isinstance(result, str) else result.getText()
