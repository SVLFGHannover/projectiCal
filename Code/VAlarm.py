class VAlarm:
    def __init__(self, description):
        self.action = ""
        self.trigger = ""
        self.duration = ""
        self.repeat = 0
        self.attach = "NULL"
        self.description = description
        self.attendeeID = "NULL"
        self.summary = ""
        self.xprop = ""
        self.ianaprop = ""

    def insertAlarm(self, db): # noch nicht mit attach
        mycursor = db.cursor()
        sql_insertAlarm = f"""\nINSERT INTO `valarm`(`action`, `trigger`, `duration`, `repeat`, `attachID`, `description`, 
                                               `attendeeID`, `summary`, `xprop`, `ianaprop`) VALUES ('{self.action}','{self.trigger}','{self.duration}',
                                               {self.repeat},{self.attach},'{self.description}',{self.attendeeID},'{self.summary}','{self.xprop}',
                                               '{self.ianaprop}') """
        try:
            mycursor.execute(sql_insertAlarm)
            db.commit()
        except:
            db.rollback()
