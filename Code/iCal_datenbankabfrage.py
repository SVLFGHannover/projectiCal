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
        self.title = 'iCalendar'
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup()

    def setup(self):
        flo = QFormLayout(self)
        linename = QLineEdit(self)
        flo.addRow('Name', linename)
        linename.editingFinished.connect(lambda: box.setText(request(linename.text())))
        linename.editingFinished.connect(lambda: btn_ics.show())
        # linemame.editingFinished.connect(QApplication.instance().quit)

        btn_q = QPushButton('Conect DB', self)
        flo.addRow(btn_q)
        btn_q.clicked.connect(lambda: box.setText(request(linename.text())))
        btn_q.clicked.connect(lambda: btn_ics.show())

        box = QTextEdit(self)
        flo.addRow('Output', box)

        btn_ics = QPushButton('Export ICS', self)
        flo.addRow(btn_ics)
        btn_ics.hide()
        # btn_ics.clicked.connect()


def request(name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User WHERE name = '" + name + "'")
    myresult = mycursor.fetchall()
    print(myresult)
    return str(myresult)


if __name__ == "__main__":
    app = QApplication([])
    window = ICal()
    window.show()
    app.exec()
