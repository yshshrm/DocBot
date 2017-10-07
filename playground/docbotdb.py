import sqlite3


class DBHelper:
    def __init__(self, dbname="myinfo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        print ("Creating table")
        stmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text, hourTake text, minTake text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text, owner, hourTake, minTake):
        stmt = "INSERT INTO items (description, owner, hourTake, minTake) VALUES (?, ?, ?, ?)"
        args = (item_text, owner, hourTake, minTake)
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
    
    def send_my_message(self, hourTake, minTake):
        stmt = "SELECT description, owner FROM items WHERE hourTake = (?) AND minTake = (?)"
        args = (hourTake, minTake, )
        return [x[0] for x in self.conn.execute(stmt, args)]
    def get_all(self, ):
        stmt = "SELECT description, owner FROM items"
        args = ( )
        return [x[0] for x in self.conn.execute(stmt, args)]