# Studienprojekt
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
