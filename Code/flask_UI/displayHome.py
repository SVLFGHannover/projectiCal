import MySQLdb.cursors
from flask import request
from flask_UI import app, db
import re
from datetime import datetime


def displayHomeEvents(sessionID):
    events = []
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ID, NAME FROM vcalendar WHERE userID = %s', (sessionID,))
    calendars_T = cursor.fetchall()
    calendars = list(calendars_T)
    cursor.execute('SELECT * FROM categories INNER JOIN vevent on categories.ID=vevent.categoriesID')
    categories = cursor.fetchall()
    cursor.execute('SELECT * FROM resources INNER JOIN vevent on resources.ID=vevent.resourcesID')
    resources = cursor.fetchall()
    for e in calendars:
        cursor.execute(f'SELECT * FROM vevent WHERE vcalendarID = {e["ID"]}')
        events_T = cursor.fetchall()
        for k in list(events_T):
            if k["dtstart"]:
                k.update({"dtstart": k["dtstart"].strftime("%d.%m.%Y, %H:%M:%S")})
            if k["dtend"]:
                k.update({"dtend": k["dtend"].strftime("%d.%m.%Y, %H:%M:%S")})
            elif k["duration"]:
                pattern = '[P]([0-9]*)[D][T]([0-9]*)[T]([0-9]*)[M]([0-9]*)[S]'
                dur_FindAll = re.findall(pattern, k["duration"])
                dur_Number = dur_FindAll[0]
                dur_Text = ["Tage", "Stunden", "Minuten", "Sekunden"]
                dur_OneException = ["ein Tag", "eine Stunde", "eine Minute", "eine Sekunde"]
                dur_OutputString = ""
                for x in range(len(dur_Text)):
                    if dur_Number[x] != "":
                        if dur_Number[x] == "1":
                            dur_OutputString += dur_OneException[x] + ", "
                        else:
                            dur_OutputString += dur_Number[x] + " " + dur_Text[x] + ", "
                k.update({'duration': dur_OutputString})
            k.update({'vcalendarID': e['NAME']})
            if k["categoriesID"]:
                for cat in categories:
                    if k["categoriesID"] == cat["ID"]:
                        k.update({'categoriesID': cat['category']})
            if k["resourcesID"]:
                for res in resources:
                    if k["resourcesID"] == res["ID"]:
                        k.update({'resourcesID': res['resource']})
            events.append(k)
            events.sort(key=lambda x: datetime.strptime(x["dtstart"], "%d.%m.%Y, %H:%M:%S"))         # Sortieren nach Startdatum
    return events
