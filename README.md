# Study Project (English Version)
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

# Studienprojekt (Deutsche Version)
Webscraping unter Anwendung von Python, Spacy, BeautifulSoup und Pandas
<br><br><br>

## Getting Started
Zuallererst wird eine Entwicklungsumgebung und Python vorausgesetzt.<br>
Wir empfehlen hierfür die Benutzung von PyCharm.
```
sudo apt-get install python3
sudo snap install pycharm-community --classic
```
Indem wir die obigen Commands im Terminal einfügen, laden wir die benötigte Programmiersprache Python und die Entwicklungsumgebung PyCharm herunter.

<br><br>
### Libraries
Nun brauchen wir bestimmte Libraries, welche für unser Projekt benötigt werden.<br>
Diese installieren wir mithilfe des Terminals durch Nutzung folgender Commands.<br><br>


```
pip install -U spacy
```
Hiermit wird Spacy heruntergeladen. Das Modul setzt sich sich mit Natural Language Processing auseinander.<br>
Mithilfe dieser Library lässt sich Text computerbasiert analysieren. Wir Nutzen es in unserem Projekt zur Selektierung Regex-basierter Patterns, zur Ermittlung von Terminangaben der gescrapten Websites.
<br><br>


```
python -m spacy download de_core_news_lg
```
Um das volle Potential von Spacy auszuschöpfen, benötigen wir eine bereits trainierte, deutschsprachige Pipeline. Diese Wird mit obigem Befehl heruntergeladen.
<br><br>


```
pip install beautifulsoup4
```
Für das Scrapen und Parsen von Website-Daten machen wir uns BeautifulSoup zunutze. Auf diese Weise können wir HTML-Files problemlos analysieren und von ungewollten Daten säubern.
<br><br>


```
pip install pandas
```
Um Datensätze zu analysieren und zu verarbeiten machen wir Gebrauch von Pandas. Entsprechendes Modul ermöglicht es uns CSV-Files zu parsen und zu erstellen. Außerdem können mit entsprechender Library fehlerhafte bzw. veraltete Datensätze herausgefiltert werden.
<br><br><br>


### Ausführen
Vorausgesetzt es wurden alle benötigten Librarys heruntergeladen, können wir uns nun dem Ausführen des Repositorys zuwenden.

```
git clone https://github.com/Avdiji/Studienprojekt.git
```
Obigen Command geben wir ein, um dieses Repository herunterzuladen.<br>
Nachdem wir das getan haben, können wir es über PyCharm öffnen und zum, unter dem "scripts"-Ordner befindlichen, run.py navigieren.<br>
Entsprechendes Python-File können wir im Run-Configurator auswählen und ausführen.<br><br>

Alternativ hat man die Möglichkeit zum bereits erwähnten Ordner zu navigieren und den unteren Befehl ausführen:
```
python run.py
```
