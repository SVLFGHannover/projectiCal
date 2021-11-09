import PyQt6.QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iCalendar"
)


class ICal(PyQt6.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'iCalendar'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup()

    def setup(self):
        tab1 = PyQt6.QtWidgets.QWidget()
        tab2 = PyQt6.QtWidgets.QWidget()

        tabs = PyQt6.QtWidgets.QTabWidget()
        tabs.addTab(tab1, 'Name')
        tabs.addTab(tab2, 'Calendar')

        tab1.layout = PyQt6.QtWidgets.QVBoxLayout(self)
        name_label = PyQt6.QtWidgets.QLabel('Name', self)

        name_line = PyQt6.QtWidgets.QLineEdit(self)
        name_line.editingFinished.connect(lambda: name_box.setText(request(name_line.text())))
        name_line.editingFinished.connect(lambda: name_btn_ics.show())

        name_btn_q = PyQt6.QtWidgets.QPushButton('Conect DB', self)
        name_btn_q.clicked.connect(lambda: name_box.setText(request(name_line.text())))
        name_btn_q.clicked.connect(lambda: name_btn_ics.show())

        name_box = PyQt6.QtWidgets.QTextEdit(self)

        name_btn_ics = PyQt6.QtWidgets.QPushButton('Export ICS', self)
        name_btn_ics.hide()

        tab1.layout.addWidget(name_label)
        tab1.layout.addWidget(name_line)
        tab1.layout.addWidget(name_btn_q)
        tab1.layout.addWidget(name_box)
        tab1.layout.addWidget(name_btn_ics)

        tab1.setLayout(tab1.layout)

        tab2.layout = PyQt6.QtWidgets.QVBoxLayout(self)
        cal_label = PyQt6.QtWidgets.QLabel('Calendar', self)

        cal_line = PyQt6.QtWidgets.QLineEdit(self)
        cal_line.editingFinished.connect(lambda: cal_box.setText(request(cal_line.text())))
        cal_line.editingFinished.connect(lambda: cal_btn_ics.show())

        cal_btn_q = PyQt6.QtWidgets.QPushButton('Conect DB', self)
        cal_btn_q.clicked.connect(lambda: cal_box.setText(request(cal_line.text())))
        cal_btn_q.clicked.connect(lambda: cal_btn_ics.show())

        cal_box = PyQt6.QtWidgets.QTextEdit(self)

        cal_btn_ics = PyQt6.QtWidgets.QPushButton('Export ICS', self)
        cal_btn_ics.hide()

        tab2.layout.addWidget(cal_label)
        tab2.layout.addWidget(cal_line)
        tab2.layout.addWidget(cal_btn_q)
        tab2.layout.addWidget(cal_box)
        tab2.layout.addWidget(cal_btn_ics)

        tab2.setLayout(tab2.layout)

        vbox = PyQt6.QtWidgets.QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


def request(name):
    q = ''
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT description, dtstart, dtend FROM VEvent WHERE attendeeID = (SELECT ID FROM user WHERE name = '" + name + "')")
    myresult = mycursor.fetchall()
    print(myresult)
    for cal in myresult:
        q += cal[0] + ' - ' + cal[1].strftime(format="%d.%m.%y %H:%M") + ' Dauer:' + str(cal[2] - cal[1]) + '\n'
    return str(q)


if __name__ == "__main__":
    app = PyQt6.QtWidgets.QApplication([])
    window = ICal()
    window.show()
    app.exec()
