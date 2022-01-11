import Export
from DB import db_insert, db_request


def insert_user(name, email):
    if name == '':
        return 'Insert Name!!'
    else:
        if Export.request_user_id(name) is None:
            werte = (name, email, '')
            sql = 'INSERT INTO User (name, email, isattendee) VALUES (%s, %s, %s)'
            db_insert(sql, werte)
            return 'User ' + name + ' added!'
        else:
            return 'User {0} exist!'.format(name)


def insert_cal(name, user, desc):
    if name == '':
        return 'Insert Name!'
    else:
        if user is None:
            return 'User not found!'
        else:
            werte = (name, user, desc, '', '', '', '')
            sql = 'INSERT INTO VCalendar (name, userID, description, prodid, version, calscale, method) VALUES (%s, ' \
                  '%s, %s, %s, %s, %s,%s) '
            db_insert(sql, werte)
            return 'Calender ' + name + ' added!'


def insert_event(summary, user, cal, stime, endtime, current, rule):
    if summary == '':
        return 'Insert Event Name!'
    else:
        if cal is None:
            return 'Calendar not found!'
        else:
            werte = (
                summary, cal, user, stime, endtime, current, current, current, rule, 0.0, 0.0, 0, 0, '', '', '', '', '',
                '', '',
                '', '', '')
            sql = 'INSERT INTO VEvent (summary, vcalendarID, attendeeID, dtstart, dtend, dtstamp, created, lastmod, ' \
                  'rruleID, geolat,geolng, priority, seq, description, uid, duration, class, location, organizer, ' \
                  'status, transp, url, recurid) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s, %s, %s, %s, ' \
                  '%s, %s,%s,%s,%s,%s) '
            db_insert(sql, werte)
            if user is None:
                return 'Event ' + summary + ' added without user!'
            else:
                return 'Event ' + summary + ' added!'


def insert_rule(rule):
    if rule == '':
        return None
    else:
        werte = (rule, '69.01.01', 0, 0, '', '', '', '', '', '', '', '', '', '')
        sql = 'INSERT INTO RRule (freq, until, count, RRule.interval, bysecond, byminute, byhour, byday, bymonthday, ' \
              'byyearday, byweekno, bymonth, bysetpos, wkst) VALUES (%s,%s,%s,%s, %s, %s, %s,%s,%s,%s,%s, %s, %s, %s) '
        db_insert(sql, werte)
        return db_request('SELECT LAST_INSERT_ID()')[0][0]


def select_events(date, name):
    if name == '':
        mess = 'Events all user: \n'
        events_req = db_request(
            "SELECT summary, dtstart, dtend, attendeeID FROM `VEvent` WHERE dtend < '{0}'".format(date))
        for ev in events_req:
            mess += str(ev[0]) + ' ' + ev[1].strftime(format="%d.%m.%y %H:%M") + ' - ' + ev[2].strftime(
                format="%d.%m.%y %H:%M") + ' - ' + Export.request_user_name(ev[3]) + '\n'
        return mess
    else:
        mess = 'Events {0}: \n'.format(name)
        id_user = Export.request_user_id(name)
        if id_user is None:
            return 'Unknown user'
        else:
            events_req = db_request(
                "SELECT summary, dtstart, dtend FROM `VEvent` WHERE dtend < '{0}' AND attendeeID = {1}".format(date,
                                                                                                               id_user))
            for ev in events_req:
                mess += str(ev[0]) + ' ' + ev[1].strftime(format="%d.%m.%y %H:%M") + ' - ' + ev[2].strftime(
                    format="%d.%m.%y %H:%M") + '\n'
            return mess
