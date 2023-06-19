import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', password='root', database='exam')  # 1
if mycon.is_connected():
    print("Successfully connected")
cursor = mycon.cursor()
cursor.execute('SELECT * FROM Book WHERE Type = "Comic";')  # 2
data = cursor.fetchall()
for rec in data:
    print(rec)
mycon.close()