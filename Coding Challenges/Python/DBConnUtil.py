import mysql.connector
from DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            properties = DBPropertyUtil.get_connection_properties()
            connection = mysql.connector.connect(**properties)
            print("Connected")
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
