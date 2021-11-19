class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.isattendee = ""

    def insertUser(self):
        sql_insertUser = f"INSERT INTO `user`(`name`, `email`, `isattendee`)" \
                     f" VALUES ('{self.name}','{self.email}','{self.isattendee}') "
        return sql_insertUser
