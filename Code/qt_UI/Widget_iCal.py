from icalendar import Calendar, Event
import PyQt6.QtWidgets
import mysql.connector

# Datenbankparameter
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iCal"
)


class ICal(PyQt6.QtWidgets.QWidget):
    # Widgetseigenschaften
    def __init__(self):
        super().__init__()
        self.title = 'iCalendar'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup()

    def setup(self):
        # Tabs definieren
        tab1 = PyQt6.QtWidgets.QWidget()
        tab2 = PyQt6.QtWidgets.QWidget()

        tabs = PyQt6.QtWidgets.QTabWidget()
        tabs.addTab(tab1, 'Event')
        tabs.addTab(tab2, 'Calendar')

        tab1.layout = PyQt6.QtWidgets.QVBoxLayout(self)
        name_label = PyQt6.QtWidgets.QLabel('Name', self)

        name_line = PyQt6.QtWidgets.QLineEdit(self)
        name_line.editingFinished.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_line.editingFinished.connect(lambda: name_btn_ics.show())

        name_btn_q = PyQt6.QtWidgets.QPushButton('Conect DB', self)
        name_btn_q.clicked.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_btn_q.clicked.connect(lambda: name_btn_ics.show())

        name_box = PyQt6.QtWidgets.QTextEdit(self)

        name_btn_ics = PyQt6.QtWidgets.QPushButton('Export ICS', self)
        name_btn_ics.clicked.connect(lambda: name_box.setText(ics_event(name_line.text())))
        name_btn_ics.hide()

        tab1.layout.addWidget(name_label)
        tab1.layout.addWidget(name_line)
        tab1.layout.addWidget(name_btn_q)
        tab1.layout.addWidget(name_box)
        tab1.layout.addWidget(name_btn_ics)

        # Tab nach Name suchen
        tab1.setLayout(tab1.layout)

        tab2.layout = PyQt6.QtWidgets.QVBoxLayout(self)
        cal_label = PyQt6.QtWidgets.QLabel('Name', self)

        cal_line = PyQt6.QtWidgets.QLineEdit(self)
        cal_line.editingFinished.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_line.editingFinished.connect(lambda: cal_btn_ics.show())

        cal_btn_q = PyQt6.QtWidgets.QPushButton('Conect DB', self)
        cal_btn_q.clicked.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_btn_q.clicked.connect(lambda: cal_btn_ics.show())

        cal_box = PyQt6.QtWidgets.QTextEdit(self)

        cal_btn_ics = PyQt6.QtWidgets.QPushButton('Export ICS', self)
        cal_btn_ics.clicked.connect(lambda: cal_box.setText(ics_cal(cal_line.text())))
        cal_btn_ics.hide()

        tab2.layout.addWidget(cal_label)
        tab2.layout.addWidget(cal_line)
        tab2.layout.addWidget(cal_btn_q)
        tab2.layout.addWidget(cal_box)
        tab2.layout.addWidget(cal_btn_ics)

        # Tab suchen nach Kalender
        tab2.setLayout(tab2.layout)

        vbox = PyQt6.QtWidgets.QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


# Suche nach name
def request_name(name):
    events = ''
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT summary, dtstart, dtend, description, rruleID  FROM VEvent WHERE attendeeID = "
        "(SELECT ID FROM user WHERE name = '" + name + "')")
    myresult_events = mycursor.fetchall()
    print(myresult_events)
    for cal in myresult_events:
        events += cal[0] + ' - ' + cal[1].strftime(format="%d.%m.%y %H:%M") + \
                  ', Dauer:' + str(cal[2] - cal[1]) + ', Beschreibung: ' + cal[3] + '\n'
        if cal[4] is None:
            events += 'Keine Wiederholung' + '\n'
    if myresult_events:
        return str(events)
    else:
        return 'Keine Events!'


# Suche nach Kalender
def request_cal(name):
    calendars = ''
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM VCalendar WHERE userID = "
        "(SELECT ID FROM user WHERE name = '" + name + "')")
    myresult_cal = mycursor.fetchall()
    print(myresult_cal)
    for cal in myresult_cal:
        calendars += str(cal[0]) + ' - ' + cal[2] + '\n'
    if myresult_cal:
        return str(calendars)
    else:
        return 'Keine Kalender!'


# Event zum Kalender zufügen
def add_event(summary, start, end, description):
    event_cal = Event()
    event_cal.add('summary', summary)
    event_cal.add('description', description)
    event_cal.add('dtstart', start)
    event_cal.add('dtend', end)
    return event_cal


# ics-Datei zu allen Events erstellen
def ics_event(name):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT summary, dtstart, dtend, description, valarmID  FROM VEvent WHERE attendeeID = "
        "(SELECT ID FROM user WHERE name = '" + name + "')")
    ics_events = mycursor.fetchall()
    if ics_events:
        cal = Calendar()
        cal.add('prodid', 'Events ' + name)
        for ev in ics_events:
            cal.add_component(add_event(ev[0], ev[1], ev[2], ev[3]))
        f = open('Events_' + name + '.ics', 'wb')
        f.write(cal.to_ical())
        f.close()
        return 'Events als ics-Datei exportiert!'
    else:
        return 'Keine Events!'


# ics-Datei für Kalender erstellen
def ics_cal(name):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM VCalendar WHERE userID = "
        "(SELECT ID FROM user WHERE name = '" + name + "')")
    myresult_cal = mycursor.fetchall()
    for cal in myresult_cal:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT summary, dtstart, dtend, description  FROM VEvent WHERE vcalendarID = " + str(cal[0]) + "")
        cal_ev = mycursor.fetchall()
        calendar = Calendar()
        calendar.add('prodid', 'Events ' + cal[2])
        for ev in cal_ev:
            calendar.add_component(add_event(ev[0], ev[1], ev[2], ev[3]))
        f = open('Events_Calendar - ' + cal[2] + '.ics', 'wb')
        f.write(calendar.to_ical())
        f.close()
    if myresult_cal:
        return 'Kalender als ics-Dateien exportiert!'
    else:
        return 'Keine Kalender!'


if __name__ == "__main__":
    app = PyQt6.QtWidgets.QApplication([])
    window = ICal()
    window.show()
    app.exec()
