class RRule:
    def __init__(self):
        self.freq = ""              # "SECONDLY", "MINUTELY", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"
        self.until = ""             # either until or count, until = datetime
        self.count = 0              # number of repetition
        self.interval = 0           # interval in relation to freq, f.e. freq = DAILY, interval = 3 -> every third day
        self.bysecond = ""          # 0 - 60
        self.byminute = ""          # 0 - 60
        self.byhour = ""            # 0 - 23
        self.byday = ""             # combination of day and number in relation to monthly/yearly in freq
        self.bymonthday = ""        # -31 - 31
        self.byyearday = ""         # -366 - 366
        self.byweekno = ""          # -53 - 53
        self.bymonth = ""           # 1 - 12
        self.bysetpos = ""          # “chooses” the 'nth' occurrence within a set of dates, must be used with by...
        self.wkst = "MO"              # Weekstart ( default Monday )

    def insertRRule(self):
        sql_InsertRRule = f"INSERT INTO `rrule` (`freq`, `until`, `count`," \
                          f" `interval`, `bysecond`, `byminute`," \
                          f"`byhour`, `byday`, `bymonthday`, `byyearday`, `byweekno`," \
                          f"`bymonth`, `bysetpos`, `wkst`) " \
                          f"VALUES" \
                          f" ('{self.freq}','{self.until}',{self.count}," \
                          f"{self.interval},'{self.bysecond}','{self.byminute}'," \
                          f"'{self.byhour}','{self.byday}','{self.bymonthday}','{self.byyearday}','{self.byweekno}'," \
                          f"'{self.bymonth}','{self.bysetpos}','{self.wkst}')"
        return sql_InsertRRule
