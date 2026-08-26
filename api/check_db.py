import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM logs").fetchall()

print(rows)

conn.close()
