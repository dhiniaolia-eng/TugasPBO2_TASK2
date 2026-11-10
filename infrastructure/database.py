import mysql.connector
from mysql.connector import Error
class Database:
    def __init__(self, host="localhost", user="root", password="", 
database="db_kampus"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Error as e:
            print(f"Error Database Connection: {e}")
            return None