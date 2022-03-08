from bs4 import BeautifulSoup
import pandas


# ----------------------------------------------------------------------------------------------------
# parameter:
#     wget_csv_row: path to a single row from the csv dataframe from Wget
#
# Method receives row from wget_dataframe and cleans the corresponding html-file
# using Beautifulsoup
#
# Returns a tuple containing a list(wget_dataframe row) and a Beautifulsoup object
# ----------------------------------------------------------------------------------------------------
def clean_html(wget_csv_row):
    wget_csv_row = wget_csv_row.split(",")
    path = wget_csv_row[1] + wget_csv_row[2]

    hlp_beautifulSoup = BeautifulSoup(open(path, "rb"), "html.parser")

    for deco in hlp_beautifulSoup(["img", "noscript", "script", "style", "head"]):
        deco.decompose()

    return wget_csv_row, hlp_beautifulSoup


# ----------------------------------------------------------------------------------------------------
# parameter:
#     wget_csv_row: a single row from the csv dataframe from Wget
#     hlp_beautifulSoup: filtered html file (Beautifulsoup object)
#
# Method finds all paragraphs in the Beautifulsoup object and appends them
# in a dictionary. Method also appends related variables from the csv dataframe
# in the dictionary
#
#
# Returns a dictionary we can use to append the data to a csv file
# ----------------------------------------------------------------------------------------------------
def segment_html(wget_csv_row, hlp_beautifulSoup):
    result = {"Choir-Name": [], "Path": [],
              "Filename": [], "<p>": [],
              "Last Update": []}

    paragraphs = hlp_beautifulSoup.find_all("p")

    for p in paragraphs:
        if not p.getText().isspace():
            result["Choir-Name"].append(wget_csv_row[0])
            result["Path"].append(wget_csv_row[1])
            result["Filename"].append(wget_csv_row[2])
            result["<p>"].append(p.getText())
            result["Last Update"].append(wget_csv_row[3])

    return result


class CleaningSegmentation:

    def __init__(self, dataframe_path, wget_dataframe_path):
        self.dataframe_path = dataframe_path
        self.wget_dataframe_path = wget_dataframe_path

    def filter_updated_dataframe(self):
        wget_dataframe = pandas.read_csv(self.wget_dataframe_path)  # Choir-Name, Path, Filename, Last Update
        seg_dataframe = pandas.read_csv(self.dataframe_path)  # Choir-Name, Path, Filename,<p>, Last Update

        concatenated = pandas.merge(seg_dataframe, wget_dataframe, on=['Choir-Name', 'Path', 'Filename', 'Last Update'],
                                    how='right', indicator=True)

        concatenated.query('_merge=="both"').drop('_merge', axis=1).to_csv(index=False)

        return concatenated.query('_merge=="right_only"').drop(['_merge','<p>'], axis=1)

    def execute_segmentation(self):
        df_update = self.filter_updated_dataframe()

        for row in df_update.iterrows():
            str_row = "".join(f"{row[1][0]},{row[1][1]},{row[1][2]},{row[1][3]}")

            clean = clean_html(str_row)
            segment = segment_html(clean[0], clean[1])
            self.create_csv(segment)

    # ----------------------------------------------------------------------------------------------------
    # parameter:
    #     append_dict: dict that contains rows of information for the segmentation - csv file
    #
    #
    # Method creates a new dataframe with the segmented html data. And appends said data to
    # the corresponding csv file
    # ----------------------------------------------------------------------------------------------------
    def create_csv(self, append_dict):
        new_dataframe = pandas.DataFrame(append_dict,
                                         columns=["Choir-Name", "Path", "Filename", "<p>", "Last Update"])

        existing_dataframe = pandas.read_csv(self.dataframe_path)

        merged_dataframe = pandas.concat([new_dataframe, existing_dataframe])
        merged_dataframe.drop_duplicates(subset=["Choir-Name", "Path", "Filename", "<p>"], inplace=True)
        merged_dataframe.to_csv(self.dataframe_path, index=False)
