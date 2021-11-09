class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.isattendee = ""

    def insertUser(self, db):
        mycursor = db.cursor()
        sql_insertUser = f"INSERT INTO `user`(`name`, `email`, `isattendee`)" \
                     f" VALUES ('{self.name}','{self.email}','{self.isattendee}') "
        try:
            mycursor.execute(sql_insertUser)
            db.commit()
        except:
            db.rollback()
