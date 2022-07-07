# Studienprojekt
Webscraping unter Anwendung von Python, Spacy, BeautifulSoup und Pandas
## Getting Started
Zu aller erst wird eine Entwicklungsumgebung und Python vorausgesetzt.<br />Wir empfehlen hierfür die Benutzung von PyCharm.
```
sudo apt-get install python3
sudo snap install pycharm-community --classic
```
Indem wir die vorgezeigten Commands im Terminal einfügen, laden wir die benötigte Programmiersprache Python und die Entwicklungsumgebung PyCharm herunter.
### Libraries
Nun brauchen wir bestimmte Libraries, welche für unser Projekt benötigt werden.<br />
Diese installieren wir mithilfe des Terminals.<br />
Nachdem wir das Terminal geöffnet haben, geben wir folgende Commands ein, um die benötigten Libraries zu installieren.
```
pip install -U spacy
```
Hiermit wird Spacy heruntergeladen, was sich mit Natural Language Processing auseinandersetzt.<br />Mithilfe dieser Library lässt sich Text computerbasiert analysieren.
```
python -m spacy download de_core_news_lg
```
Hiermit wird die für Spacy benötigte deutsche Pipeline heruntergeladen.
```
pip install beautifulsoup4
```
Hiermit wird die Library Beautiful Soup heruntergeladen, welche für das Scrapen und Parsen von Website-Daten benötigt wird.
```
pip install pandas
```
Hiermit laden wir die Library Pandas herunter, welche sich mit der Verarbeitung und Analyse von Daten beschäftigt.
### Ausführen
```
git clone https://github.com/Avdiji/Studienprojekt.git
```
Diesen Command geben wir ein, um das Repository herunterzuladen.<br />
Nachdem wir das getan haben, können wir es über PyCharm öffnen und zu run.py unter Scripts navigieren.<br />
Letztendlich müssen wir nun nur noch run.py ausführen.
