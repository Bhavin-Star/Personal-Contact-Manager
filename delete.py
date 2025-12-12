import sqlite3

conn  = sqlite3.connect("data.db")
cur = conn.cursor()

name = input("Enter the name you want to delete: ")

cur.execute("DELETE FROM CONTACTS WHERE CONTACT_NAME = ?", (name,))
conn.commit()
