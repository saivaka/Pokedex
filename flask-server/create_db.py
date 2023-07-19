import sqlite3
connection = sqlite3.connect('database.db')


try:
    with open('sql/schema.sql') as f:
        connection.executescript(f.read())
        print("Database has been connected")
except:
    print("Database already is connected")


connection.commit()
connection.close()