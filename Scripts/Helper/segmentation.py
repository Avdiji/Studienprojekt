from datetime import datetime
# TODO save text of each paragraph in a csv using pandas


# ----------------------------------------------------------------------------------------------------
# Class is used to segment the cleaned HTML - Files into different
# categories (date, contact, location...)
# ----------------------------------------------------------------------------------------------------
class Segmentation:

    @staticmethod
    def get_time():
        time = datetime.now()
        return print(time.strftime("%d/%m/%Y %H:%M:%S"))
