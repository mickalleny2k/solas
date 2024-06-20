import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="solas"
)

cursor = db.cursor()
sql="insert into candidates (id, name,party,constituency, years) values (%s,%s,%s,%s,%s)"
id = input ("Enter id: ")
name = input ("Enter name: ")
party = input ("Enter party: ")
constituency = input ("Enter constituency: ")
years = input ("Enter years: ")
values = (id,name,party,constituency, years)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()