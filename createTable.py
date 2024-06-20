import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="solas"
)

cursor = db.cursor()
sql="CREATE TABLE candidates (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), party VARCHAR(250), constituency VARCHAR(250), years INT)"
cursor.execute(sql)

db.close()
cursor.close()