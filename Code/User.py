import mysql.connector

class User:
    def __init__(self, name, email, isattendee):
        self.name = name
        self.email = email
        self.isattendee = isattendee

    def insertIntoDB(self):
        insertUser = f"INSERT INTO `user`(`name`, `email`, `isattendee`) VALUES ({name},{email},{isattendee})"
        mycursor = mydb.cursor()
        mycursor.execute(insertUser)
        mycursor.commit()
