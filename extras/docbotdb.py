import sqlite3


class DBHelper:
    def __init__(self, dbname="info.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        print ("Creating table")
        stmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text, hour_take text, min_take text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text, owner, hour_take, ):
        stmt = "INSERT INTO items (description, owner, hour_take, min_take) VALUES (?, ?, ?, ?)"
        args = (item_text, owner, hour_take, min_take)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, owner):
        stmt = "DELETE FROM items WHERE owner = (?)"
        args = ( owner )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, owner):
        stmt = "SELECT description FROM items WHERE owner = (?)"
        args = (owner, )
        return [x[0] for x in self.conn.execute(stmt, args)]
    
    def send_my_message(self, hour_take, min_take):
        stmt = "SELECT description, owner FROM items WHERE hour_take = (?) AND min_take = (?)"
        args = (hour_take, min_take)
        return [x[0] for x in self.conn.execute(stmt, args)]