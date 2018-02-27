import sqlite3
import uuid
import os

class DB:
    def __init__(self):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.subs_db = self.dir+'/db/subscribers.db'
        self.my_mail = self.dir+'/db/mail.db'
        self.conn = sqlite3.connect(self.subs_db)
    
    def create_table(self):
        self.conn.execute('''CREATE TABLE SUBSCRIBERS
         (ID varchar(250) PRIMARY KEY,
         MAIL varchar(250) NOT NULL);''')
    
    def add_subs(self, mail):
        self.conn.execute("""INSERT INTO SUBSCRIBERS (ID,MAIL)
                     VALUES ('{}', '{}');""".format(str(uuid.uuid4()), mail) );
        self.conn.commit()
    
    def remove_subs(self, mail):
        self.conn.execute("DELETE from SUBSCRIBERS where MAIL = "+mail+";")
        self.conn.commit()
    
    def view_subs(self):
        self.cursor = self.conn.execute("SELECT id, mail from SUBSCRIBERS")
        return self.cursor
    
    def close_conn(self):
        self.conn.close()

#db = DB()
##db.create_table()
#db.add_subs('aremij7@gmail.com')
#for row in db.view_subs():
#    print(row)
#db.close_conn()
