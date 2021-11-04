class User:
    def __init__(self, name, email, isattendee):
        self.name = name
        self.email = email
        self.isattendee = isattendee

    def insertUser(self):
        sql_insertUser = f"INSERT INTO `user`(`name`, `email`, `isattendee`)" \
                     f" VALUES ({self.name},{self.email},{self.isattendee}) "
        return sql_insertUser
