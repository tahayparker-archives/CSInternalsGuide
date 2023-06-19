import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', password='root', database='exam')  # Statement 1
if mycon.is_connected():
    print("Successfully connected")
cursor = mycon.cursor()
cursor.execute('SELECT StuID, Name FROM student WHERE Class LIKE "11%"')   # Statement 2
data = cursor.fetchall()
for rec in data:
    print(rec)
mycon.close()