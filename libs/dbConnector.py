import sqlite3
import random

class SQLiteConnector():
  def __init__(self, dbname: str):
    self.name = dbname
    con = sqlite3.connect(f"./data/{self.name}.db")
    con.execute("DROP TABLE IF EXISTS 'clients'")
    con.execute("CREATE TABLE IF NOT EXISTS  clients(ip, port, code)")
    con.execute("CREATE TABLE IF NOT EXISTS  users(username, password)")
    con.close()

  def addClient(self, ip: str, port: int):
    with sqlite3.connect(f"./data/{self.name}.db") as con:
      code = str(random.randint(100, 999)) + "-" + str(random.randint(100, 999))
      con.execute(f"INSERT INTO clients VALUES ('{ip}', {port}, '{code}')")
      con.commit()
    return code