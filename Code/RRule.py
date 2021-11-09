class RRule:
    def __init__(self):
        self.freq = ""
        self.until = ""
        self.count = 0
        self.interval = 0
        self.bysecond = ""
        self.byminute = ""
        self.byhour = ""
        self.byday = ""
        self.bymonthday = ""
        self.byyearday = ""
        self.byweekno = ""
        self.bymonth = ""
        self.bysetpos = ""
        self.wkst = ""

    def insertRRule(self, db):
        mycursor = db.cursor()
        sql_InsertRRule = f"INSERT INTO `rrule` (`freq`, `until`, `count`," \
                          f" `interval`, `bysecond`, `byminute`," \
                          f"`byhour`, `byday`, `bymonthday`, `byyearday`, `byweekno`," \
                          f"`bymonth`, `bysetpos`, `wkst`) " \
                          f"VALUES" \
                          f" ('{self.freq}','{self.until}',{self.count}," \
                          f"{self.interval},'{self.bysecond}','{self.byminute}'," \
                          f"'{self.byhour}','{self.byday}','{self.bymonthday}','{self.byyearday}','{self.byweekno}'," \
                          f"'{self.bymonth}','{self.bysetpos}','{self.wkst}')"
        print(sql_InsertRRule)
        try:
            mycursor.execute(sql_InsertRRule)
            db.commit()
        except:
            db.rollback()