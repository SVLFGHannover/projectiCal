from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDateTime
from Export import *
from Insert import *


class ICal(QWidget):
    # Widgetseigenschaften
    def __init__(self):
        super().__init__()
        self.title = 'iCalendar'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setup()

    def setup(self):
        # Tabs definieren
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        tab5 = QWidget()
        tab6 = QWidget()
        tab7 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Insert')
        tabs.addTab(tab2, 'Export')

        insert_tab = QTabWidget()
        insert_tab.addTab(tab3, 'Event')
        insert_tab.addTab(tab4, 'Calendar')
        insert_tab.addTab(tab5, 'User')

        export_tab = QTabWidget()
        export_tab.addTab(tab6, 'Event')
        export_tab.addTab(tab7, 'Calender')

        tab1.layout = QVBoxLayout(self)
        tab1.layout.addWidget(insert_tab)
        tab1.setLayout(tab1.layout)

        tab2.layout = QVBoxLayout(self)
        tab2.layout.addWidget(export_tab)
        tab2.setLayout(tab2.layout)

        tab3.layout = QVBoxLayout(self)

        event_nam_label = QLabel('Event')
        event_name_line = QLineEdit(self)

        event_cal_label = QLabel('Calendar')
        event_cal_line = QLineEdit(self)

        event_user_label = QLabel('User (optional)')
        event_user_line = QLineEdit(self)

        stat_label = QLabel('Start')
        date_start = QDateTimeEdit(QDateTime.currentDateTime().toPyDateTime())
        date_start.setDisplayFormat('yyyy-MM-dd hh:mm')

        end_label = QLabel('End')
        date_end = QDateTimeEdit(QDateTime.currentDateTime().toPyDateTime())
        date_end.setDisplayFormat('yyyy-MM-dd hh:mm')

        even_rule_label = QLabel('Repeat')
        event_rule = QComboBox()
        event_rule.addItem('')
        event_rule.addItem('DAILY')
        event_rule.addItem('WEEKLY')
        event_rule.addItem('MONTHLY')
        event_rule.addItem('YEARLY')

        event_insert_btn = QPushButton('Insert', self)
        event_insert_btn.clicked.connect(lambda: event_insert_box.setText(
            insert_event(event_name_line.text(), request_user_id(event_user_line.text()),
                         request_calendar_id(event_cal_line.text()),
                         date_start.text(), date_end.text(),
                         QDateTime.currentDateTime().toPyDateTime(), insert_rule(event_rule.currentText()))))

        event_insert_box = QTextEdit()

        tab3.layout.addWidget(event_nam_label)
        tab3.layout.addWidget(event_name_line)
        tab3.layout.addWidget(event_cal_label)
        tab3.layout.addWidget(event_cal_line)
        tab3.layout.addWidget(event_user_label)
        tab3.layout.addWidget(event_user_line)
        tab3.layout.addWidget(stat_label)
        tab3.layout.addWidget(date_start)
        tab3.layout.addWidget(end_label)
        tab3.layout.addWidget(date_end)
        tab3.layout.addWidget(even_rule_label)
        tab3.layout.addWidget(event_rule)
        tab3.layout.addWidget(event_insert_btn)
        tab3.layout.addWidget(event_insert_box)

        tab3.setLayout(tab3.layout)

        tab4.layout = QVBoxLayout(self)
        cal_nam_label = QLabel('Name')
        cal_name_line = QLineEdit(self)

        cal_user_label = QLabel('User')
        cal_user_line = QLineEdit(self)

        cal_desc_label = QLabel('Description')
        cal_desc_line = QLineEdit(self)

        cal_btn = QPushButton('Insert', self)
        cal_btn.clicked.connect(lambda: cal_insert_box.setText(
            insert_cal(cal_name_line.text(), request_user_id(cal_user_line.text()), cal_desc_line.text())))

        cal_insert_box = QTextEdit(self)

        tab4.layout.addWidget(cal_nam_label)
        tab4.layout.addWidget(cal_name_line)
        tab4.layout.addWidget(cal_user_label)
        tab4.layout.addWidget(cal_user_line)
        tab4.layout.addWidget(cal_desc_label)
        tab4.layout.addWidget(cal_desc_line)
        tab4.layout.addWidget(cal_btn)
        tab4.layout.addWidget(cal_insert_box)
        tab4.setLayout(tab4.layout)

        tab5.layout = QVBoxLayout(self)

        user_label = QLabel('Name')
        user_line = QLineEdit(self)

        email_label = QLabel('Email')
        email_line = QLineEdit(self)

        user_btn = QPushButton('Insert', self)
        user_btn.clicked.connect(lambda: user_box.setText(insert_user(user_line.text(), email_line.text())))

        user_box = QTextEdit(self)

        tab5.layout.addWidget(user_label)
        tab5.layout.addWidget(user_line)
        tab5.layout.addWidget(email_label)
        tab5.layout.addWidget(email_line)
        tab5.layout.addWidget(user_btn)
        tab5.layout.addWidget(user_box)

        tab5.setLayout(tab5.layout)

        tab6.layout = QVBoxLayout(self)

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

        tab6.layout.addWidget(name_label)
        tab6.layout.addWidget(name_line)
        tab6.layout.addWidget(name_btn_q)
        tab6.layout.addWidget(name_box)
        tab6.layout.addWidget(name_btn_ics)

        tab6.setLayout(tab6.layout)

        tab7.layout = QVBoxLayout(self)

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

        tab7.layout.addWidget(cal_label)
        tab7.layout.addWidget(cal_line)
        tab7.layout.addWidget(cal_btn_q)
        tab7.layout.addWidget(cal_box)
        tab7.layout.addWidget(cal_btn_ics)

        tab7.setLayout(tab7.layout)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication([])
    window = ICal()
    window.show()
    app.exec()
