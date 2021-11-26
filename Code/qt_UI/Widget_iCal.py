from datetime import timedelta
from icalendar import Calendar, Event, Alarm
from PyQt6.QtWidgets import *
import mysql.connector

# Datenbankparameter
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iCal"
)


class ICal(QWidget):
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
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Event')
        tabs.addTab(tab2, 'Calendar')

        tab1.layout = QVBoxLayout(self)
        name_label = QLabel('Name', self)

        name_line = QLineEdit(self)
        name_line.editingFinished.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_line.editingFinished.connect(lambda: name_btn_ics.show())

        name_btn_q = QPushButton('Conect DB', self)
        name_btn_q.clicked.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_btn_q.clicked.connect(lambda: name_btn_ics.show())

        name_box = QTextEdit(self)

        name_btn_ics = QPushButton('Export ICS', self)
        name_btn_ics.clicked.connect(lambda: name_box.setText(ics_event(name_line.text())))
        name_btn_ics.hide()

        tab1.layout.addWidget(name_label)
        tab1.layout.addWidget(name_line)
        tab1.layout.addWidget(name_btn_q)
        tab1.layout.addWidget(name_box)
        tab1.layout.addWidget(name_btn_ics)

        # Tab nach Name suchen
        tab1.setLayout(tab1.layout)

        tab2.layout = QVBoxLayout(self)
        cal_label = QLabel('Name', self)

        cal_line = QLineEdit(self)
        cal_line.editingFinished.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_line.editingFinished.connect(lambda: cal_btn_ics.show())

        cal_btn_q = QPushButton('Conect DB', self)
        cal_btn_q.clicked.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_btn_q.clicked.connect(lambda: cal_btn_ics.show())

        cal_box = QTextEdit(self)

        cal_btn_ics = QPushButton('Export ICS', self)
        cal_btn_ics.clicked.connect(lambda: cal_box.setText(ics_cal(cal_line.text())))
        cal_btn_ics.hide()

        tab2.layout.addWidget(cal_label)
        tab2.layout.addWidget(cal_line)
        tab2.layout.addWidget(cal_btn_q)
        tab2.layout.addWidget(cal_box)
        tab2.layout.addWidget(cal_btn_ics)

        # Tab suchen nach Kalender
        tab2.setLayout(tab2.layout)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


# Suche nach name
def request_name(name):
    events = ''
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT summary, dtstart, dtend, description, rruleID  FROM VEvent WHERE attendeeID = "
        "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    myresult_events = mycursor.fetchall()
    print(myresult_events)
    for cal in myresult_events:
        events += cal[0] + ' - ' + cal[1].strftime(format="%d.%m.%y %H:%M") + \
                  ', Dauer:' + str(cal[2] - cal[1]) + ', Beschreibung: ' + cal[3] + '\n'
        if cal[4] is None:
            events += 'Keine Wiederholung' + '\n'
        else:
            mycursor.execute("SELECT freq FROM RRule WHERE ID = {0}".format(cal[4]))
            rule = mycursor.fetchall()[0][0]
            events += 'Wiederholung - ' + rule + '\n'
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
        "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    myresult_cal = mycursor.fetchall()
    print(myresult_cal)
    for cal in myresult_cal:
        calendars += 'Kalender - ' + cal[2] + '\n'
    if myresult_cal:
        return str(calendars)
    else:
        return 'Keine Kalender!'


# Event zum Kalender zufügen
def add_event(summary, start, end, description, alarm, rule):
    event_cal = Event()
    event_cal.add('summary', summary)
    event_cal.add('description', description)
    event_cal.add('dtstart', start)
    event_cal.add('dtend', end)

    if rule is not None:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT freq, RRule.interval, until FROM RRule WHERE ID = {0}".format(str(rule)))
        rrule = mycursor.fetchall()[0]
        event_cal.add('rrule', {'freq': rrule[0], 'interval': rrule[1], 'until': rrule[2]})

    if alarm is not None:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT action, summary, description, VAlarm.trigger, "
            "VAlarm.repeat, duration FROM VAlarm WHERE ID = {0}".format(
                str(alarm)))
        al = mycursor.fetchall()[0]
        event_cal.add_component(add_alarm(al))

    return event_cal


# Alarm zufügen
def add_alarm(al):
    alarm = Alarm()
    alarm.add('action', al[0])
    alarm.add('summary', al[1])
    alarm.add('descriptiom', al[2])
    alarm.add('trigger', timedelta(minutes=-int(al[3])))
    alarm.add('repeat', al[4])
    alarm.add('duration', timedelta(minutes=+int(al[5])))
    return alarm


# ics-Datei zu allen Events erstellen
def ics_event(name):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT summary, dtstart, dtend, description, valarmID, rruleID  FROM VEvent WHERE attendeeID = "
        "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    ics_events = mycursor.fetchall()
    if ics_events:
        cal = Calendar()
        cal.add('prodid', 'Events ' + name)
        for ev in ics_events:
            cal.add_component(add_event(ev[0], ev[1], ev[2], ev[3], ev[4], ev[5]))
        ics = save_dialog('Speichern Events von ' + name)
        if ics == '':
            return 'Keine Events exportiert!'
        else:
            f = open(ics + '.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
            return 'Events als ics-Datei exportiert!'
    else:
        return 'Keine Events!'


# ics-Datei für Kalender erstellen
def ics_cal(name):
    mess = ''
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM VCalendar WHERE userID =(SELECT ID FROM user WHERE name = '{0}')".format(name))
    myresult_cal = mycursor.fetchall()
    if myresult_cal:
        for cal in myresult_cal:
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT summary, dtstart, dtend, description, valarmID, "
                "rruleID  FROM VEvent WHERE vcalendarID = {0}".format(
                    str(cal[0])))
            cal_ev = mycursor.fetchall()
            calendar = Calendar()
            calendar.add('prodid', 'Events ' + cal[2])
            for ev in cal_ev:
                calendar.add_component(add_event(ev[0], ev[1], ev[2], ev[3], ev[4], ev[5]))
            ics = save_dialog('Speichern Events von Kalender ' + cal[2])
            if ics == '':
                mess += 'Keine Events von Kalender {0} exportiert!'.format(str(cal[2])) + '\n'
            else:
                f = open(ics + '.ics', 'wb')
                f.write(calendar.to_ical())
                f.close()
                mess += 'Events von Kalender {0} als ics-Datei exportiert!'.format(str(cal[2])) + '\n'
        return mess
    else:
        return 'Keine Kalender!'


def save_dialog(name):
    n = QFileDialog.getSaveFileName(caption=name)
    return n[0]


if __name__ == "__main__":
    app = QApplication([])
    window = ICal()
    window.show()
    app.exec()
