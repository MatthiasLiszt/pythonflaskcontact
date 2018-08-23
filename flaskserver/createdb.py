import sqlite3

db = sqlite3.connect('database')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE msg(id INTEGER PRIMARY KEY, subject TEXT,message TEXT)
''')
db.commit()
db.close()