import sqlite3

conn  = sqlite3.connect("data.db")
cur = conn.cursor()

no = int(input("Enter phone no you want to search: "))


getname = conn.execute("SELECT * FROM CONTACTS WHERE CONTACT_PH_NO = ?", (no,))

for i in getname:
    print(i)
