class VCalendar:
    def __init__(self, userID, name, description, prodid, version, calscale, method, xprop, ianaprop):
        self.userID = userID
        self.name = name
        self.description = description
        self.prodid = prodid
        self.version = version
        self.calscale = calscale
        self.method = method
        self.xprop = xprop
        self.ianaprop = ianaprop

    def InsertCalendar(self):
        sql_insertCalendar = f"INSERT INTO `vcalendar`(`userID`, `name`, `description`, `prodid`," \
                             f" `version`, `calscale`, `method`, `xprop`, `ianaprop`)" \
                        f"VALUES ({self.userID},{self.name},{self.description},{self.prodid}," \
                         f"{self.version},{self.calscale},{self.method},{self.xprop}, {self.ianaprop})"
        return sql_insertCalendar