import datetime

from flask_UI import app, db
from flask_mysqldb import MySQL
import MySQLdb.cursors
from coop.VEvent import VEvent, insertCategory, insertResources, insertContact
from flask import request
from coop.RRule import RRule
from coop.VAlarm import VAlarm


def getCalendars(sessionid):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT name FROM vcalendar WHERE userID = %s', (sessionid,))
    calendars = cursor.fetchall()
    return calendars


def getEndDate(event):
    if request.form["end_date"]:
        end_date = request.form["end_date"]
        end_time = request.form["end_time"]
        dtend = end_date + " " + end_time
        event.dtend = dtend
    else:
        dur_sec = request.form["dur_sec"]
        dur_min = request.form["dur_min"]
        dur_hour = request.form["dur_hour"]
        dur_days = request.form["dur_day"] + 7*request.form["dur_week"]
        event.duration = "P" + str(dur_days) + "DT" + str(dur_hour) + "T" + str(
            dur_min) + "M" + str(dur_sec) + "S"


def rruleRest(event, rrule):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.form["rr_count"]:
        rrule.count = request.form["rr_count"]
    elif request.form["rr_until"]:
        rrule.until = request.form["rr_until"]
    sql_rrule = rrule.insertRRule()
    cursor.execute(sql_rrule)
    db.connection.commit()
    event.dic_ID["rruleID"] = "(SELECT ID FROM rrule ORDER BY ID DESC LIMIT 1)"


def getRRule(event):
    rrule = RRule()
    if request.form["rr_hourly"]:
        rrule.freq = "HOURLY"
        rrule.interval = request.form["rr_hourly"]
    elif request.form["rr_daily"]:
        rrule.freq = "DAILY"
        rrule.interval = request.form["rr_daily"]
    elif request.form["rr_weekly"]:
        rrule.freq = "WEEKLY"
        rrule.interval = request.form["rr_weekly"]
        selected_weekdays = request.form.getlist("rr_weekdays")
        rrule.byday = ', '.join(selected_weekdays)
    elif request.form["rr_monthly"]:
        rrule.freq = "MONTHLY"
        rrule.interval = request.form["rr_monthly"]
    elif request.form["rr_yearly"]:
        rrule.freq = "YEARLY"
        rrule.interval = request.form["rr_yearly"]

    rruleRest(event, rrule)

    return event


def getVAlarmMainAttributes(valarm):  # trigger, duration, repeat for valarm
    valarm.trigger = "-P" + str(request.form["whenA_day"]) + "DT" + str(
        request.form["whenA_hour"]) + "T" + str(request.form["whenA_min"]) + "M" + str(
        request.form["whenA_sec"]) + "S"
    valarm.duration = "P" + str(request.form["durA_day"]) + "DT" + str(
        request.form["durA_hour"]) + "T" + str(request.form["durA_min"]) + "M" + str(
        request.form["durA_sec"]) + "S"
    valarm.repeat = request.form["countA"]


def getVAlarm(event):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.form["emailT_A"]:
        valarm = VAlarm("EMAIL")
        getVAlarmMainAttributes(valarm)
        valarm.summary = request.form["emailT_A"]
        cursor.execute('SELECT ID FROM user WHERE email = %s',
                       (request.form["emailA_A"],))
        attendeeCatch = cursor.fetchone()
        if attendeeCatch:
            valarm.attendeeID = attendeeCatch["ID"]
        else:
            attendee = User("", request.form["emailA_A"])
            cursor.execute(attendee.insertUser())
            db.connection.commit()
            valarm.attendeeID = "(SELECT ID FROM user ORDER BY ID DESC LIMIT 1)"
        sql_alarm = valarm.insertAlarm()
        cursor.execute(sql_alarm)
        db.connection.commit()
        event.dic_ID["valarmID"] = "(SELECT ID FROM valarm ORDER BY ID DESC LIMIT 1)"

    elif request.form["display_A"]:
        valarm = VAlarm("DISPLAY")
        getVAlarmMainAttributes(valarm)
        valarm.description = request.form["display_A"]
        sql_alarm = valarm.insertAlarm()
        cursor.execute(sql_alarm)
        db.connection.commit()
        event.dic_ID["valarmID"] = "(SELECT ID FROM valarm ORDER BY ID DESC LIMIT 1)"
        """elif request.form["sound_A"]:
            valarm = VAlarm("AUDIO")
            getVAlarmMainAttributes(valarm)
            cursor.execute(f"INSERT INTO attach ('attachment') VALUES ( NULL )") # weiß nicht weiter
            db.connection.commit()
            valarm.attach = "(SELECT ID FROM attach ORDER BY ID DESC LIMIT 1)
            sql_alarm = valarm.insertAlarm()
            cursor.execute(sql_alarm)
            db.connection.commit()
            event.dic_ID["valarmID"] = "(SELECT ID FROM valarm ORDER BY ID DESC LIMIT 1)"""


def getOther(other, table, column):
    if other:
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_other = f"INSERT INTO {table}({column}) VALUES ('{other}')"
        cursor.execute(sql_other)
        db.connection.commit()
        otherID = "(SELECT ID FROM {} ORDER BY ID DESC LIMIT 1)".format(table)
    else:
        otherID = "NULL"
    return otherID


def fillGeoData(lat, lon, city, street, event):
    if lat and lon:
        event.geolat = lat
        event.geolng = lon
    elif city:
        event.location = city + ", " + street
    return event


def createE(sessionID):
    name_E = request.form["name_E"]
    beschreibung_E = request.form["beschreibung_E"]
    calendarname = request.form["calendars"]
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ID FROM vcalendar WHERE name = %s AND userID = %s', (calendarname, sessionID,))
    calendarCatch = cursor.fetchone()
    calendarID = calendarCatch["ID"]
    start_date = request.form["start_date"]
    start_time = request.form["start_time"]
    dtstart = start_date + " " + start_time
    event = VEvent(name_E, beschreibung_E, dtstart, calendarID)  # Creating Event Object for easier handling
    getVAlarm(event)
    getEndDate(event)  # Duration or Dtend
    getRRule(event)

    fillGeoData(request.form["lat"], request.form["lon"], request.form["city"], request.form["street"], event)

    event.dic_ID["categoriesID"] = getOther(request.form["category"], "CATEGORIES", "CATEGORY")
    event.dic_ID["resourcesID"] = getOther(request.form["resources"], "RESOURCES", "RESOURCE")
    event.dic_ID["contactID"] = getOther(request.form["contact"], "CONTACT", "CONTACT")

    event.uid = f"{datetime.datetime.now()}|PID|IPAdress"

    print(event.insertEvent())
    return event
