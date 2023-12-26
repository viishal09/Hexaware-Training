import mysql.connector as connection

from DBPropertyUtil import PropertyUtil

class dbConnection:
    def init(self):
        pass

    def open(self):
        try:
            data = PropertyUtil.getPropertyString()
            self.conn_str = connection.connect(host=data[0], database=data[3], username=data[1], password=data[2])
            if self.conn_str.is_connected():
                print("--Database Is Connected--")
                self.mycursor = self.conn_str.cursor()
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.conn_str.close()
            print('Connection Closed.')
        except Exception as e:
            print(e)

