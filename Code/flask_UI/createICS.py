from icalendar import Calendar, Event
from flask_UI import app, db
import MySQLdb.cursors
from flask import request


def createICSfromEvent(eventID):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f'SELECT * FROM vevent WHERE ID = {eventID}')
    event = cursor.fetchone()
    print(event)
    cursor.execute(f'SELECT * FROM vcalendar WHERE ID = {event["vcalendarID"]}')
    calendar = cursor.fetchone()
    c = Calendar()
    e = Event()
    c["name"] = calendar["name"]
    c["description"] = calendar["description"]
    c["prodid"] = calendar["prodid"]

    e["summary"] = event["summary"]
    e["dtstart"] = event["dtstart"]
    e["created"] = event["created"]
    e["description"] = event["description"]

    if event["duration"]:
        e["duration"] = event["duration"]
    else:
        e["dtend"] = event["dtend"]

    if event["categoriesID"]:
        cursor.execute(f'SELECT category FROM categories WHERE ID = {event["categoriesID"]}')
        catch = cursor.fetchone()
        e.add("category", catch["category"])

    c.add_component(e)
    f = open(e["summary"] + '.ics', 'wb')
    f.write(c.to_ical())
    f.close()
    return e["summary"] + ".ics"


def createICSfromCalendar(calendarID):
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f'SELECT * FROM vevent WHERE vcalendarID = {calendarID}')
    events = cursor.fetchall()
    print(events)
    cursor.execute(f'SELECT * FROM vcalendar WHERE ID = {calendarID}')
    calendar = cursor.fetchone()
    c = Calendar()
    c["name"] = calendar["name"]
    c["description"] = calendar["description"]
    c["prodid"] = calendar["prodid"]
    e = Event()
    for event in events:

        e["summary"] = event["summary"]
        e["dtstart"] = event["dtstart"]
        e["created"] = event["created"]
        e["description"] = event["description"]

        if event["duration"]:
            e["duration"] = event["duration"]
        else:
            e["dtend"] = event["dtend"]

        if event["categoriesID"]:
            cursor.execute(f'SELECT category FROM categories WHERE ID = {event["categoriesID"]}')
            catch = cursor.fetchone()
            e["category"] = catch["category"]
        e_copy = e.copy()   # otherwise clear didn't work like intended
        c.add_component(e_copy)
        e.clear()
    f = open(c["name"] + '.ics', 'wb')
    f.write(c.to_ical())
    f.close()
    return c["name"] + ".ics"
