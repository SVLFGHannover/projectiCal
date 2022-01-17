# projectiCal

Speicherung/GUI von Kalenderdaten und Generierung von iCalendar-Dateien

## Einführung

Dieses Projekt entstand während der Ausbildung zum Fachinformatiker in der SVLFG. Das Programm dient als Kalender, welche angelehnt sind an das iCalendar-Dateiformat. 
Nähere Informationen können auf der [Homepage](https://icalendar.org) nachgelesen  werden. 
Eine ausführliche Dokumentation ist [hier](https://icalendar.org/RFC-Specifications/iCalendar-RFC-5545/) zu finden.
Die Hauptfunktionen der Applikation sind das Erstellen von
- Usern
-	Kalendern
-	Events
-	iCalendar-Dateien

Das Projekt wurde in Python geschrieben, ist jedoch aufgeteilt. Es gibt eine Flask- und eine QT-Lösung. Die Programme sind an eine MariaDB-Datenbank angeknüpft, welche über xamp läuft. Die verwendete Datenbank ist bei beiden Applikationen identisch.

## Einrichten der Datenbank 


Im Ordner Dokumentation ist die Datei "Anleitung Datenbank iCal erstellen.pdf" zu finden. Diese beschreibt, wie die benötigte Datenbank erstellt wird.

## QT

### Technologies

### Setup

## 4 Flask

### 4.1 Technologies
Die folgenden Pakete werden verwendet und müssen beim Starten des Programms
- Flask
- Flask_mysqldb
- MySQL-python
- MySQL-python-connector
- icalendar
- re
- datetime

Die Pakete re und datetime sind built-in bei Python. Für die restlichen imports wurde das Paketverwaltungsprogramm pip verwendet.

```python
pip install MySQL-python
pip install MySQL-python-connector
pip install Flask
pip install flask_mysqldb
pip install icalendar
```

### 4.2 Setup

Die Webanwendung läuft auf dem vom Flask-Paket bereitgestellten Entwicklungsserver. 
Dieser wird im Pythonfile main_Flask.py gestartet.

![Screenshot 2022-01-17 091259](https://user-images.githubusercontent.com/69800773/149732014-abdffe7b-02a3-48b1-a497-63a4aae18847.png)

Folgendes sollte nun erscheinen. 
![image](https://user-images.githubusercontent.com/69800773/149731793-06d8e838-fa50-44a4-8ade-a21cbb42e642.png)

Mit dem Link kann nun auf die Startseite navigiert werden.
Bevor die Applikation verwendet werden kann, muss noch die Datenverbindung mithilfe von xampp aufgebaut werden. Dies wurde bereits im Abschnitt Einrichten der Datenbank erklärt. 
