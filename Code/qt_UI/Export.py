from PyQt6.QtWidgets import QFileDialog
from icalendar import Calendar, Event, Alarm
from datetime import timedelta
from Insert import *


def show_user():
    user = ''
    myresult_user = db_request("SELECT name FROM User")
    for usr in myresult_user:
        user += usr[0] + '\n'
    return user


def show_cal():
    cal = ''
    myresult_cal = db_request("SELECT name, userID FROM VCalendar")
    for c in myresult_cal:
        cal += c[0] + ', User - ' + request_user_name(c[1]) + '\n'
    return cal


def request_user_id(name):
    myresult_user = db_request("SELECT id FROM User Where name = '{0}'".format(name))
    if not myresult_user:
        return None
    else:
        return myresult_user[0][0]


def request_user_name(id_user):
    myresult_user = db_request("SELECT name FROM User Where ID = '{0}'".format(id_user))
    return myresult_user[0][0]


def request_calendar_id(name):
    myresult_user = db_request("SELECT ID FROM VCalendar WHERE name = '{0}'".format(name))
    if not myresult_user:
        return None
    else:
        return myresult_user[0][0]


def request_rule_id(rule):
    if rule == '':
        return None
    else:
        myresult_rule = db_request("SELECT ID FROM RRule WHERE freq = '{0}'".format(rule))
        return myresult_rule[0][0]


# Suche nach name
def request_name(name):
    events = ''
    myresult_events = db_request("SELECT summary, dtstart, dtend, description, rruleID  FROM VEvent WHERE attendeeID = "
                                 "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    for cal in myresult_events:
        events += cal[0] + ' - ' + cal[1].strftime(format="%d.%m.%y %H:%M") + \
                  ', Duration:' + str(cal[2] - cal[1]) + ', Description: ' + cal[3] + '\n'
        if cal[4] is None:
            events += 'No Repetition' + '\n'
        else:
            rule = db_request("SELECT freq FROM RRule WHERE ID = {0}".format(cal[4]))[0][0]
            events += 'Repeat - ' + rule + '\n'
    if myresult_events:
        return str(events)
    else:
        return 'No Events!'


# Suche nach Kalender
def request_cal(name):
    calendars = ''
    myresult_cal = db_request("SELECT * FROM VCalendar WHERE userID = "
                              "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    for cal in myresult_cal:
        calendars += 'Calender - ' + cal[2] + '\n'
    if myresult_cal:
        return str(calendars)
    else:
        return 'No Calenders!'


# Event zum Kalender zufügen
def add_event(summary, start, end, description, alarm, rule, dtstamp):
    event_cal = Event()
    event_cal.add('uid', 'user')
    event_cal.add('summary', summary)
    event_cal.add('description', description)
    event_cal.add('dtstamp', dtstamp)
    event_cal.add('dtstart', start)
    event_cal.add('dtend', end)

    if rule is not None:
        rrule = db_request("SELECT freq, RRule.interval, until FROM RRule WHERE ID = {0}".format(str(rule)))[0]
        event_cal.add('rrule', {'freq': rrule[0], 'interval': rrule[1], 'until': rrule[2]})

    if alarm is not None:
        al = db_request("SELECT action, summary, description, VAlarm.trigger, "
                        "VAlarm.repeat, duration FROM VAlarm WHERE ID = {0}".format(str(alarm)))[0]
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
    ics_events = db_request(
        "SELECT summary, dtstart, dtend, description, valarmID, rruleID, dtstamp  FROM VEvent WHERE attendeeID = "
        "(SELECT ID FROM user WHERE name = '{0}')".format(name))
    if ics_events:
        cal = Calendar()
        cal.add('prodid', 'Events ' + name)
        cal.add('version', '2.0')
        for ev in ics_events:
            cal.add_component(add_event(ev[0], ev[1], ev[2], ev[3], ev[4], ev[5], ev[6]))
        ics = save_dialog('Save Events from ' + name)
        if ics == '':
            return 'No Events exported!'
        else:
            f = open(ics + '.ics', 'wb')
            f.write(cal.to_ical())
            f.close()
            return 'Events as ics-File exportiert!'
    else:
        return 'No Events!'


# ics-Datei für Kalender erstellen
def ics_cal(name):
    mess = ''
    myresult_cal = db_request(
        "SELECT * FROM VCalendar WHERE userID =(SELECT ID FROM user WHERE name = '{0}')".format(name))
    if myresult_cal:
        for cal in myresult_cal:
            cal_ev = db_request("SELECT summary, dtstart, dtend, description, valarmID, "
                                "rruleID, dtstamp  FROM VEvent WHERE vcalendarID = {0}".format(str(cal[0])))
            calendar = Calendar()
            calendar.add('prodid', 'Events ' + cal[2])
            cal.add('version', '2.0')
            for ev in cal_ev:
                calendar.add_component(add_event(ev[0], ev[1], ev[2], ev[3], ev[4], ev[5], ev[6]))
            ics = save_dialog('Save Events from Calender ' + cal[2])
            if ics == '':
                mess += 'No Events from Calender {0} exported!'.format(str(cal[2])) + '\n'
            else:
                f = open(ics + '.ics', 'wb')
                f.write(calendar.to_ical())
                f.close()
                mess += 'Events from Calender {0} as ics-File exported!'.format(str(cal[2])) + '\n'
        return mess
    else:
        return 'No Calender!'


def save_dialog(name):
    n = QFileDialog.getSaveFileName(caption=name)
    return n[0]
