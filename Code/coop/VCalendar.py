class VCalendar:
    def __init__(self, userID, name, description):
        self.userID = userID
        self.name = name
        self.description = description
        self.prodid = "SVLFG//iCalendar"                                 # Product Identifier, Default: SVLFG//iCalendar
        self.version = "2.0"
        self.calscale = "gregorian"                                      # Art des Kalenders
        self.method = ""                                                 # ?
        self.xprop = "NULL"                                              # ?
        self.ianaprop = "NULL"                                           # ?

    def insertCalendar(self):
        sql_insertCalendar = f"INSERT INTO VCALENDAR(USERID, NAME, DESCRIPTION, PRODID," \
                             f" VERSION, CALSCALE, METHOD, XPROP, IANAPROP)" \
                             f"VALUES ({self.userID},'{self.name}','{self.description}','{self.prodid}'," \
                             f"'{self.version}','{self.calscale}','{self.method}',{self.xprop}, {self.ianaprop})"
        return sql_insertCalendar
