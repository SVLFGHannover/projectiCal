import mysql.connector


class VEvent:
    def __init__(self):
        self.description = None
        self.summary = None
        self.class_ = None
        self.priority = None
        self.dtstamp = None
        self.dtstart = None
        self.dtend = None
        self.duration = None
        self.created = None
        self.lastmod = None
        self.dic_ID = {"rruleID": 0, "vcalendarID": 0, "valarmID": 0, "resourcesID": 0,
                       "relatedID": 0, "rstatus": 0, "rdateID": 0, "recurid": 0,
                       "attachID": 0, "attendeeID": 0, "categoriesID": 0, "commentID": 0,
                       "contactID": 0, "exdateID": 0, "xpropID": 0, "ianapropID": 0}
        self.geolat = None
        self.geolong = None
        self.location = None
        self.organizer = None
        self.uid = None
        self.seq = None
        self.status = None
        self.transp = None
        self.url = None

    def InsertEvent(self):
        sql_insertEvent = f"INSERT INTO `vevent`" \
                          f"(`description`, `dtstamp`, `uid`, `dtstart`, `dtend`, `duration`, `class `, `created`," \
                          f" `geolat`, `geolng`, `lastmod`, `location`, `organizer`, `priority`, `seq`, `status`," \
                          f" `summary`, `transp`, `url`, `recurid`, `attachID`, `attendeeID`, `categoriesID`, `commentID`," \
                          f" `contactID`, `exdateID`, `rstatusID`, `relatedID`, `resourcesID`, `rdateID`, `xpropID`," \
                          f" `ianapropID`, `valarmID`, `rruleID`, `vcalendarID`)" \
                          f"VALUES" \
                          f" ('{description}', '{dtstamp}', '{uid}', '{dtstart}', '{dtend}', '{duration}', '{class_}', '{created}'," \
                          f" '{geolat}', '{geolng}', '{lastmod}', '{location}', '{organizer}', '{priority}', '{seq}', '{status}'," \
                          f" '{summary}', '{transp}', '{url}', '{dic_ID['recurid']}', '{dic_ID['attachID']}', '{dic_ID['attendeeID']}'," \
                          f" '{dic_ID['categoriesID']}', '{dic_ID['commentID']}'," \
                          f" '{dic_ID['contactID']}', '{dic_ID['exdateID']}', '{dic_ID['rstatusID']}', '{dic_ID['relatedID']}'," \
                          f" '{dic_ID['resourcesID']}', '{dic_ID['rdateID']}', '{dic_ID['xpropID']}', '{dic_ID['ianapropID']}'," \
                          f" '{dic_ID['valarmID']}', '{dic_ID['rruleID']}', '{dic_ID['vcalendarID']}')"
        return sql_insertEvent


def insertCategory(newCategory):
    sql_insertCategory = f"INSERT INTO `Categories`(`category`) VALUES ({newCategory})"
    try:
        cursor.execute(sql_insertCategory)
        mydb.commit()
    except:
        mydb.rollback()
    return sql_insertCategory


def insertContact(newContact):
    mycursor = mydb.cursor()
    sql_insertContact = f"INSERT INTO `Contact`(`contact`) VALUES ('{newContact}')"
    try:
        mycursor.execute(sql_insertContact)
        mydb.commit()
    except:
        mydb.rollback()
    return sql_insertContact


def insertResource(newResource):
    global mydb
    mycursor = mydb.cursor()
    sql_insertResource = f"INSERT INTO RESOURCES(RESOURCE) VALUES ('{newResource}')"
    try:
        mycursor.execute(sql_insertResource)
        mydb.commit()
    except:
        mydb.rollback()
    return sql_insertResource