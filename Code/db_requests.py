# alle Benutzer mit Name "name" werden als dictonary ausgegeben
# z.B. bei Peter - [(2, 'Peter', 'email@me.com', 'i')]
def request_user(name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User WHERE name = '" + name + "'")
    myresult = mycursor.fetchall()
    return myresult

# es werden die emails der Benutzer mit Name "name" als dictonary ausgegeben
def request_email(name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT email FROM User WHERE name = '" + name + "'")
    myresult = mycursor.fetchall()
    return myresult

# es werden alle Calendars der Benutzer mit Name "name" als dictonary ausgegeben
def request_calendar(name):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM VCalendar WHERE userID = (SELECT ID FROM user WHERE name = '" + name + "')")
    myresult = mycursor.fetchall()
    return myresult

# es werden alle Events der Benutzer mit Name "name" als dictonary ausgegeben
def request_event(name):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM VEvent WHERE attendeeID = (SELECT ID FROM user WHERE name = '" + name + "')")
    myresult = mycursor.fetchall()
    return myresult