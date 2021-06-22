
from datetime import date
import mysql.connector

class MysqlConn():

  def __init__(self, db):
    self.db_connection = mysql.connector.connect(
      host=db['host'], 
      user=db['user'], 
      passwd=db['passwd'], 
      database=db['database']
    )
    self.cursor = self.db_connection.cursor()

  def query(self, query):
    self.cursor.execute(query)
    return self.cursor

  def set_db(self, database):
    self.db_connection = mysql.connector.connect(
      host=db['host'], 
      user=db['user'], 
      passwd=db['passwd'], 
      database=database
    )
    self.cursor = self.db_connection.cursor()  

  def commit(self):
    self.db_connection.commit()

  def disconnect(self):
    self.cursor.close()
    self.db_connection.commit()
    self.db_connection.close()