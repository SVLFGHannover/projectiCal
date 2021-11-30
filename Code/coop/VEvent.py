import datetime


class VEvent:
    def __init__(self, summary, description, dtstart, vcalendarID):
        self.description = description
        self.summary = summary                                                      # Title of Event
        self.class_ = ""                                                       # Access classification ( public / private )
        self.priority = 0                                                      # 1 (lowest) - 9 (highest), 0 = undefined
        self.dtstamp = datetime.datetime.now()                                 # Time of Creation
        self.dtstart = dtstart                                                 # Starting time of event
        self.dtend = ""                                                     # Ending time of event
        self.duration = ""                                                     # Alternative to dtend, duration of event
        self.created = datetime.datetime.now()                           # Same as dtstamp
        self.lastmod = ""                                                # Date of last modification of iCalendar-Object
        self.recurid = ""                                                      # Identifier for repetition of event
        self.vcalendarID = vcalendarID
        self.dic_ID = {"rruleID": "NULL", "valarmID": "NULL", "resourcesID": "NULL",
                       "relatedID": "NULL", "rstatusID": "NULL", "rdateID": "NULL",
                       "attachID": "NULL", "attendeeID": "NULL", "categoriesID": "NULL", "commentsID": "NULL",
                       "contactID": "NULL", "exdateID": "NULL", "xpropID": "NULL", "ianapropID": "NULL"}
        self.geolat = 0.0                                                  # Latitude of location
        self.geolng = 0.0                                                  # Longitude of location
        self.location = ""                                          # Alternative to geolat, geolng, address of location
        self.organizer = ""
        self.uid = ""                                               # Identifier for the event, Date|Time|PID|@|IPAdress
        self.seq = 0                                                # Number of modifications
        self.status = ""                                            # tentative / confirmed / cancelled
        self.transp = ""                                            # Identifier, if an event takes time ( either opaque or transparent )
        self.url = ""                                                       # Link to the iCalendar-Object

    def insertEvent(self):
        sql_insertEvent = "INSERT INTO `vevent`(`description`, `dtstamp`, `uid`, `dtstart`, `dtend`, " \
                          "`duration`, `class`, `created`, `geolat`, `geolng`, `lastmod`, `location`, " \
                          "`organizer`, `priority`, `seq`, `status`, `summary`, `transp`, `url`, `recurid`, " \
                          "`attachID`, `attendeeID`, `categoriesID`, `commentID`, `contactID`, `exdateID`, " \
                          "`rstatusID`, `relatedID`, `resourcesID`, `rdateID`, `xpropID`, `ianapropID`, " \
                          f"`valarmID`, `rruleID`, `vcalendarID`) VALUES ('{self.description}','{self.dtstamp}'," \
                          f"'{self.uid}','{self.dtstart}','{self.dtend}','{self.duration}','{self.class_}','{self.created}','{self.geolat}'," \
                          f"'{self.geolng}','{self.lastmod}','{self.location}','{self.organizer}',{self.priority},{self.seq}," \
                          f"'{self.status}','{self.summary}','{self.transp}','{self.url}','{self.recurid}',{self.dic_ID['attachID']}," \
                          f"{self.dic_ID['attendeeID']},{self.dic_ID['categoriesID']}, {self.dic_ID['commentsID']}," \
                          f"{self.dic_ID['contactID']},{self.dic_ID['exdateID']}, {self.dic_ID['rstatusID']}," \
                          f"{self.dic_ID['relatedID']},{self.dic_ID['resourcesID']},{self.dic_ID['rdateID']}," \
                          f"{self.dic_ID['xpropID']},{self.dic_ID['ianapropID']},{self.dic_ID['valarmID']}," \
                          f"{self.dic_ID['rruleID']},{self.vcalendarID})"
        return sql_insertEvent


def insertCategory(newCategory):
    sql_insertContact = f"INSERT INTO CATEGORIES(CATEGORY) VALUES ('{newCategory}')"
    return sql_insertContact


def insertContact(newContact):
    sql_insertContact = f"INSERT INTO CONTACT(CONTACT) VALUES ('{newContact}')"
    return sql_insertContact


def insertResources(newResource):
    sql_insertResources = f"INSERT INTO RESOURCES(RESOURCE) VALUES ('{newResource}')"
    return sql_insertResources
