import sqlite3

conn = sqlite3.connect("data.db")
cur  = conn.cursor()

contact = """CREATE TABLE CONTACTS
(CONTACT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
CONTACT_NAME VARCHAR(255) NOT NULL,
CONTACT_EMAIL VARCHAR(255) NOT NULL,
CONTACT_PH_NO INTGER NOT NULL)"""

cur.execute(contact)
conn.close()


