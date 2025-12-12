import sqlite3

conn = sqlite3.connect("data.db")
cur  = conn.cursor()

getdata = conn.execute("SELECT * FROM CONTACTS")
for i  in getdata:
    print(i)

