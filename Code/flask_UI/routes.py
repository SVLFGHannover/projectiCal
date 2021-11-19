from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_UI import app, db
from flask_mysqldb import MySQL
import MySQLdb.cursors
from coop.User import User
from coop.VCalendar import VCalendar
from coop.VEvent import VEvent

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
            msg = 'Incorrect username/password!'
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
        """events = None
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ID FROM vcalendar WHERE userID = %s', (session["ID"],))
        calendars_T = cursor.fetchall()
        calendars = list(calendars_T)
        print(calendars[0])
        for e in calendars:
            for x, y in e.items():
                print(x)
                cursor.execute('SELECT * FROM vevent WHERE ID = %s', (y))
                events_T = cursor.fetchall()
                events.add(events_T)
        print(events)"""
        return render_template("home.html", loggedin=True, msg="")
    return render_template("home.html", msg="", loggedin=False)


@app.route("/createEvent", methods=['GET', 'POST'])
def createEvent():
    if 'loggedin' in session:
        # Dropdown Calendars
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT name FROM vcalendar WHERE userID = %s', (session["ID"],))
        calendars = cursor.fetchall()
        calendars_L = list(calendars)
        if request.method == 'POST':
            name_E = request.form["name_E"]
            beschreibung_E = request.form["beschreibung_E"]
            calendarname = request.form["test"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT ID FROM vcalendar WHERE name = %s AND userID = %s', (calendarname, session["ID"],))
            calendarCatch = cursor.fetchone()
            calendarID = calendarCatch["ID"]
            start_date, start_time, end_date, end_time = "", "", "", ""

            try:
                start_date = request.form["start_date"]
                start_time = request.form["start_time"]
                dtstart = start_date + " " + start_time
                end_date = request.form["end_date"]
                end_time = request.form["end_time"]
                dtend = end_date + " " + end_time
            except:
                print("")
            event = VEvent(name_E, beschreibung_E, dtstart, dtend, calendarID)

            return render_template("createEvent.html", title='Account', loggedin=True, calendars=calendars_L, msg="Event wurde erstellt")
        return render_template("createEvent.html", title='Account', loggedin=True, calendars=calendars_L)
    else:
        redirect(url_for('home'))


@app.route("/createCalendar", methods=['GET', 'POST'])
def createCalendar():
    if 'loggedin' in session:
        if request.method == 'POST' and 'name_C' in request.form:
            # Create variables for easy access
            name = request.form['name_C']
            try:
                beschreibung = request.form['beschreibung']
            except:
                beschreibung = ""
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM vcalendar WHERE name = %s', (name,))
            calender = cursor.fetchone()
            if calender:
                msg = 'Calendar already exists!'
            else:
                vcalendar = VCalendar(session["ID"], name, beschreibung)
                cursor.execute(vcalendar.insertCalendar())
                msg="Kalender wurde erstellt."
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
        cursor.execute('SELECT * FROM user WHERE name = %s', (name,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            user = User(name, email)
            cursor.execute(user.insertUser())
            db.connection.commit()
            calendar = VCalendar('(SELECT ID FROM user ORDER BY ID DESC LIMIT 1)', "Hauptkalendar",
                                 name + "s Startkalender")
            cursor.execute(calendar.insertCalendar())
            db.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)
