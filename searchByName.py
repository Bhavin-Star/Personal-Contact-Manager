import sqlite3

conn  = sqlite3.connect("data.db")
cur = conn.cursor()

name = input("Enter name you want to search: ")


getname = conn.execute("SELECT * FROM CONTACTS WHERE CONTACT_NAME = ?", (name,))

for i in getname:
    print(i)
