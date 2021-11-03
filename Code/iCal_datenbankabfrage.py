from PyQt6.QtWidgets import QWidget, QApplication, \
    QPushButton, QLineEdit, QFormLayout, QTextEdit
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iCalendar"
)


class ICal(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('iCalendar')
        flo = QFormLayout(self)
        linename = QLineEdit(self)

        flo.addRow('Name', linename)


        btn_q = QPushButton('Conect DB', self)
        flo.addRow(btn_q)



        box = QTextEdit(self)
        flo.addRow('Output', box)

        self.setGeometry(100, 100, 500, 500)


def request(name):

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User WHERE name = '" + name + "'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)



if __name__ == "__main__":
    app = QApplication([])
    window = ICal()
    window.show()
    app.exec()
