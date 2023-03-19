import sqlite3

class DatabaseConnection:
    """ When the DatabaseConnection class is initialized with something like 
        `db = DatabaseConnection()` 
        This will call the __init__ function and will setup our database for runtime
        :param db_file: database_file in string format
        :return Connection object or None
    """
    def __init__(self):
            # self.name = db_name
            # # connect takes url, dbname, user-id, password
            # self.conn = self.connect(db_name)
            # self.cursor = self.conn.cursor()
            print("INITIALIZED")
    
    """ Creating a database connection to the SQLite db specified by the passed in db_file var.
        :param db_file: database_file in string format
        :return Connection object or None
    """
    def create_conn(self, db_file):
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

a = DatabaseConnection()

