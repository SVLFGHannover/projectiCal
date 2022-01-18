from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['SECRET_KEY'] = '0953eb3999aa7fbf714749b3c962ba22'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'iCal'

# Intialize MySQL
db = MySQL(app)

from flask_UI import routes
