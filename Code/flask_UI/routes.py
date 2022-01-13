import datetime

from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_UI import app, db
from flask_mysqldb import MySQL
import MySQLdb.cursors
from coop.User import User
from coop.VCalendar import VCalendar
from coop.VEvent import VEvent, insertCategory, insertResources, insertContact
from coop.VAlarm import VAlarm
from coop.RRule import RRule
from flask_UI.createEvent import *
from flask_UI.createICS import *
from flask_UI.displayHome import *


@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form:
        name = request.form['name']
        email = request.form['email']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE name = %s AND email = %s', (name, email,))
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['ID'] = account['ID']
            session['name'] = account['name']
            return redirect(url_for('home'))
        else:
            msg = 'Falscher Name oder falsche Email!'
    return render_template('home.html', msg=msg)


@app.route('/about')
def about():
    if 'loggedin' in session:
        return render_template("about.html", loggedin=True, title="About")
    return render_template("about.html", msg="", loggedin=False, title="About")


@app.route("/")
@app.route("/home")
def home():
    if 'loggedin' in session:
        events = displayHomeEvents(session["ID"])
        return render_template("home.html", loggedin=True, msg="", events=events)
    return render_template("home.html", msg="", loggedin=False)


@app.route("/createEvent", methods=['GET', 'POST'])
def createEvent():
    if 'loggedin' in session:
        calendars = getCalendars(session["ID"])  # Select all Calendars for Dropdown menu
        calendars_L = list(calendars)

        if request.method == 'POST':
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            event = createE(session["ID"])                   # create Event from Inputform
            cursor.execute(event.insertEvent())  # Insert VEvent into DB
            db.connection.commit()

            return render_template("createEvent.html", title='Account', loggedin=True, calendars=calendars_L,
                                   msg="Event wurde erstellt")
        return render_template("createEvent.html", title='Account', loggedin=True, calendars=calendars_L)
    else:
        redirect(url_for('home'))  # site can only be accessed when logged in


@app.route("/createCalendar", methods=['GET', 'POST'])
def createCalendar():
    if 'loggedin' in session:
        if request.method == 'POST' and 'name_C' in request.form:
            # Create variables for easy access
            name = request.form['name_C']
            beschreibung = request.form['beschreibung']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM vcalendar WHERE name = %s', (name,))
            calender = cursor.fetchone()
            if calender:
                msg = 'Dieser Kalender existiert bereits!'
            else:
                vcalendar = VCalendar(session["ID"], name, beschreibung)
                cursor.execute(vcalendar.insertCalendar())
                msg = "Kalender wurde erstellt."
                db.connection.commit()
            return render_template("createCalendar.html", title='create Calendar', loggedin=True, msg=msg)
        else:
            return render_template("createCalendar.html", title='create Calendar', loggedin=True)
    else:
        redirect(url_for('home'))


@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form:
        # Create variables for easy access
        name = request.form['name']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Diese Email wird bereits verwendet.'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            user = User(name, email)
            cursor.execute(user.insertUser())
            db.connection.commit()
            calendar = VCalendar('(SELECT ID FROM user ORDER BY ID DESC LIMIT 1)', "Hauptkalendar",
                                 name + "s Startkalender")
            cursor.execute(calendar.insertCalendar())
            db.connection.commit()
            msg = 'Du wurdest erfolgreich registriert!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/createICS', methods=['GET', 'POST'])
def createICS():
    if session["loggedin"]:
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM vcalendar WHERE userID = %s', (session["ID"],))
        calendars_T = cursor.fetchall()
        calendars = list(calendars_T)
        return render_template("createICS.html", loggedin=True, msg="", calendars=calendars)
    else:
        redirect(url_for('home'))


@app.route('/createICSEvent', methods=['GET', 'POST'])
def createICSEvent():
    if request.method == 'POST':
        if 'eventID' in request.form:
            icsString = createICSfromEvent(request.form["eventID"])
            output = f"Die Datei {icsString}.ics wurde erstellt."
            return render_template("info.html", info=output, loggedin=True)
        if 'calendarID' in request.form:
            icsString = createICSfromCalendar(request.form["calendarID"])
            output = f"Die Datei {icsString}.ics wurde erstellt."
            return render_template("info.html", info=output, loggedin=True)
    else:
        redirect(url_for('home'))


@app.route('/info', methods=['GET', 'POST'])
def info():
    if session["loggedin"]:
        return render_template("info.html", info="", loggedin=True)
    else:
        redirect(url_for('home'))


@app.route('/deleteEvent', methods=['GET', 'POST'])
def deleteEvent():
    if request.method == 'POST' and "deleteID" in request.form:
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f'SELECT summary from vevent WHERE ID={request.form["deleteID"]};')
        catch = cursor.fetchone()
        cursor.execute(f'DELETE from vevent WHERE ID={request.form["deleteID"]};')
        db.connection.commit()
        output = f"Der Termin {catch['summary']} wurde gelöscht."
        return render_template("info.html", info=output, loggedin=True)
    else:
        redirect(url_for('home'))
