import sqlite3

"""
so the db is the main place for character storage and trait tracking. Would we want to modify that often? if not we could probably just write the contents
of the database to a file and leave it alone. instead of reading it every time the program starts it would already be loaded. 


TODO: SQL stuff
initialization - open the db file and check values are not empty?
upload - upload a csv to the running player.db
download - get current running db as csv


#The way to use this class is by first importing the module. so if we are the root: 
from database import db
# now we can create a d object that can be passed around or use one of the functions tied to the obj defined
# in this script. 
d = db.DatabaseConnection()
d.check_db()
"""


""" When the DatabaseConnection class is initialized with something like 
    `db = DatabaseConnection()` 
    This will call the __init__ function and will setup our database for runtime
    :param db_file: database_file in string format
    :return Connection object or None
"""
class DatabaseConnection:
    def __init__(self):
            self.db_file = "player.db"

            # should we handle errs here?
            self.conn = self.connect(self.db_file)
            self.cursor = self.conn.cursor()

    """ Creating a database connection to the SQLite db specified by the passed in db_file var.
        :param db_file: database_file in string format
        :return Connection object or None
    """
    def connect(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            # should probably add some logging as well. but for now prints are MVP
            print(e)
            return conn

    """ Creating a database table in the specified connection with the desiried table name
        :param db_file: connection to the sqlite3 database with the specific db for input
        :param table_name: the table to create 
        :return True or False - Bool based on success or failure. 
    """
    def create_table(self, conn, table_name):
        try:
            c = conn.cursor()
            c.execute(table_name)
        except Error as e:
            print(e)

## future work to build the write_db func. just getting the db out of the running memory back into disk in the event of a crash. 
## or we want to deploy elsewhere. 
    def write_db(self):
        print("this should be used to write to the db file so we can make changes later")


## We can use this function for checking the state of the db. do the tables equal the number expected?
## does the players equal the number expected?
    def check_db(self):
        try:
            c = self.conn.cursor()
            res = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        except Error as e:
            print(e)
        # check and make sure it's not empty
        print(res)

# this will be done to get the current status of the sqlite3 db. we can use this later for stats and stuff
    def status(self):
        try:
            c = self.conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        except Error as e:
            print(e)
        print(c.fetchall())


