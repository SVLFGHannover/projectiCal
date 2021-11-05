class RRule:
    def __init__(self):
        self.freq = None
        self.until = None
        self.count = None
        self.interval = None
        self.bysecond = None
        self.byminute = None
        self.byhour = None
        self.byday = None
        self.bymonthday = None
        self.byyearday = None
        self.byweekno = None
        self.bymonth = None
        self.bysetpos = None
        self.wkst = None

    def InsertRRule(self):
        sql_InsertRRule = f"INSERT INTO 'rrule' (`freq`, `until`, `count`," \
                          f" `interval`, `bysecond`, `byminute`," \
                          f"`byhour`, `byday`, `bymonthday`, `byyearday`, `byweekno`," \
                          f"`bymonth`, `bysetpos`, `wkst`) " \
                          f"VALUES" \
                          f" ('{freq}','{until}','{count}'," \
                          f"'{interval}','{bysecond}','{byminute}'," \
                          f"'{byhour}','{byday}','{bymonthday}','{byyearday}','{byweekno}'," \
                          f"'{bymonth}','{bysetpos}','{wkst}')"
        return sql_InsertRRule