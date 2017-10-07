import sqlite3


class DBHelper:
    def __init__(self, dbname="info.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        print ("creating table")
        stmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text, time_take text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text, owner, time_take):
        stmt = "INSERT INTO items (description, owner, time_take) VALUES (?, ?, ?)"
        args = (item_text, owner, time_take)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text, owner):
        stmt = "DELETE FROM items WHERE description = (?) AND owner = (?)"
        args = (item_text, owner )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, owner):
        stmt = "SELECT description FROM items WHERE owner = (?)"
        args = (owner, )
        return [x[0] for x in self.conn.execute(stmt, args)]
    
    def send_my_message(self, time_take, owner):
        stmt = "SELECT description FROM items WHERE owner = (?) AND time_take = (?)"
        args = (owner, time_take)
        return [x[0] for x in self.conn.execute(stmt, args)]