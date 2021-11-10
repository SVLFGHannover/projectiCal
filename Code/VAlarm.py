class VAlarm:
    def __init__(self):
        self.action = ""                    # AUDIO / DISPLAY / EMAIL
        self.trigger = ""                   # Duration or Datetime, when the alarm starts ( positive or negative )
        self.duration = ""                  # indicates how long it takes to repeat the alarm
        self.repeat = 0                     # Number of repetitions
        self.attach = "NULL"                # attached files ( f.e. sound for audio alarm )
        self.description = ""      # displayed text, when action = DISPLAY
        self.attendeeID = "NULL"            # when action = EMAIL, which attendees get an email ( should be different table relationship? )
        self.summary = ""                   # displayed text, when action = EMAIL
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
