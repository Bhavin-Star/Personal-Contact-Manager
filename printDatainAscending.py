import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

getData = conn.execute("SELECT * FROM CONTACTS order by CONTACT_NAME")

for i  in getData:
    print(i)
    
