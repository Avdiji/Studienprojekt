# Studienprojekt
Webscraping using Python, Spacy, BeautifulSoup und Pandas
<br><br><br>

## Getting Started
First of all, a development environment and Python are required.<br>
We recommend using PyCharm for this.
```
sudo apt-get install python3
sudo snap install pycharm-community --classic
```
By inserting the commands shown above in the terminal, we download the required programming language Python and the development environment PyCharm.

<br><br>
### Libraries
We now need certain libraries, which are required for our project.<br>
We install them with the help of the terminal by using the following commands.<br><br>


```
pip install -U spacy
```
This will download Spacy. The module deals with Natural Language Processing.<br>
With the help of this library text can be analyzed computer-based. We use it in our project to select regex-based patterns, to identify relevant dates of the scrapped websites.
<br><br>


```
python -m spacy download de_core_news_lg
```
To utilize spacy's full potential, we need an already trained, German language pipeline. This will be downloaded with the command shown above.
<br><br>


```
pip install beautifulsoup4
```
For scraping and parsing website data we use BeautifulSoup. This way we can easily analyze HTML files and clean them from unwanted data.
<br><br>


```
pip install pandas
```
To analyze and process datasets we make use of Pandas. This module allows us to parse and create CSV files. In addition, with this library, incorrect or outdated datasets can be filtered out.
<br><br><br>


### Execute
Assuming that all required libraries have been downloaded, we can now start running the repository.

```
git clone https://github.com/Avdiji/Studienprojekt.git
```
We enter the command above to download this repository.<br>
After we have done that, we can open it via PyCharm and navigate to the run.py located under the "scripts" folder.<br>
This Python file we can select and run in the run configurator.<br><br>

Alternatively, you have the option to navigate to the folder already mentioned and run the command below:
```
python run.py
```
