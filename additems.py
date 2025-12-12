import sqlite3

conn  = sqlite3.connect("data.db")
cur = conn.cursor()
while True:
    name = input("Enter ur name: ")
    mail = input("Enter ur Email: ")
    ph = int(input("Enter ur no: "))

    t = (name, mail, ph)

    contact =  """ INSERT INTO CONTACTS
    (CONTACT_NAME, CONTACT_EMAIL, CONTACT_PH_NO)
    VALUES(?,?,?)"""

    cur.execute(contact,t)
    ask = input("Do you want to add more elemts: ")
    if(ask == 'no'):
        break

conn.commit()