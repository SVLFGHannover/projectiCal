import mysql.connector

# Datenbankparameter
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='iCal'
)


def set_conn(host, user, pw, db):
    try:
        mydb.host = host
        mydb.set_login(user, pw)
        mydb.database = db
        return 'Database connected successfull!'
    except mysql.connector.Error as err:
        return 'Database not connected!{}'.format(err)


def db_request(req):
    mycursor = mydb.cursor()
    mycursor.execute(req)
    return mycursor.fetchall()


def db_insert(s, w):
    mycursor = mydb.cursor()
    mycursor.execute(s, w)
    mydb.commit()

def db_del(req):
    mycursor = mydb.cursor()
    mycursor.execute(req)
    mydb.commit()
