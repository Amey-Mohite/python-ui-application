import sqlite3 as sql

class DatabaseConnection: # database connection
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sql.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

def createOrderTable(): # creating a table
    with DatabaseConnection('Database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE Product(product_id integer primary key,price integer)')#,no_of_item integer