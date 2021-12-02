from PyQt6.QtWidgets import *
from Logik import *
from DB import set_conn


class ICal(QWidget):
    # Widgetseigenschaften
    def __init__(self):
        super().__init__()
        self.title = 'iCalendar'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup()

    def setup(self):
        # Tabs definieren
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Event')
        tabs.addTab(tab2, 'Calendar')
        tabs.addTab(tab3, 'Databse')

        # Tab nach Name suchen
        tab1.layout = QVBoxLayout(self)
        name_label = QLabel('Name', self)

        name_line = QLineEdit(self)
        name_line.editingFinished.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_line.editingFinished.connect(lambda: name_btn_ics.show())

        name_btn_q = QPushButton('Seaarch Events', self)
        name_btn_q.clicked.connect(lambda: name_box.setText(request_name(name_line.text())))
        name_btn_q.clicked.connect(lambda: name_btn_ics.show())

        name_box = QTextEdit(self)

        name_btn_ics = QPushButton('Export ICS', self)
        name_btn_ics.clicked.connect(lambda: name_box.setText(ics_event(name_line.text())))
        name_btn_ics.hide()

        tab1.layout.addWidget(name_label)
        tab1.layout.addWidget(name_line)
        tab1.layout.addWidget(name_btn_q)
        tab1.layout.addWidget(name_box)
        tab1.layout.addWidget(name_btn_ics)

        tab1.setLayout(tab1.layout)

        # Tab suchen nach Kalender
        tab2.layout = QVBoxLayout(self)
        cal_label = QLabel('Name', self)

        cal_line = QLineEdit(self)
        cal_line.editingFinished.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_line.editingFinished.connect(lambda: cal_btn_ics.show())

        cal_btn_q = QPushButton('Search Calender', self)
        cal_btn_q.clicked.connect(lambda: cal_box.setText(request_cal(cal_line.text())))
        cal_btn_q.clicked.connect(lambda: cal_btn_ics.show())

        cal_box = QTextEdit(self)

        cal_btn_ics = QPushButton('Export ICS', self)
        cal_btn_ics.clicked.connect(lambda: cal_box.setText(ics_cal(cal_line.text())))
        cal_btn_ics.hide()

        tab2.layout.addWidget(cal_label)
        tab2.layout.addWidget(cal_line)
        tab2.layout.addWidget(cal_btn_q)
        tab2.layout.addWidget(cal_box)
        tab2.layout.addWidget(cal_btn_ics)

        tab2.setLayout(tab2.layout)

        # Tab suchen Datenbank
        tab3.layout = QVBoxLayout(self)
        host_label = QLabel('Host', self)
        host_line = QLineEdit(self)
        user_label = QLabel('User', self)
        user_line = QLineEdit(self)
        pw_label = QLabel('Password', self)
        pw_line = QLineEdit(self)
        pw_line.setEchoMode(QLineEdit.EchoMode.Password)
        db_label = QLabel('Database', self)
        db_line = QLineEdit(self)

        db_btn_q = QPushButton('Connect Database', self)
        db_btn_q.clicked.connect(
            lambda: db_box.setText(set_conn(host_line.text(), user_line.text(), pw_line.text(), db_line.text())))

        db_box = QTextEdit(self)

        tab3.layout.addWidget(host_label)
        tab3.layout.addWidget(host_line)
        tab3.layout.addWidget(user_label)
        tab3.layout.addWidget(user_line)
        tab3.layout.addWidget(pw_label)
        tab3.layout.addWidget(pw_line)
        tab3.layout.addWidget(db_label)
        tab3.layout.addWidget(db_line)
        tab3.layout.addWidget(db_btn_q)
        tab3.layout.addWidget(db_box)

        tab3.setLayout(tab3.layout)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication([])
    window = ICal()
    window.show()
    app.exec()
