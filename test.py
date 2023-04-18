import sqlite3

base = sqlite3.connect("db.sqlite3")

cur = base.cursor()

arr = ['1', '001', '10:00:00', '0', '24', '57', '750', '20', '600', '0', '1', '0']


cur.execute("INSERT INTO cloud_cabinet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(arr[0]), arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[1], arr[1], arr[1], arr[1], arr[1], arr[1], arr[1]))
base.commit()