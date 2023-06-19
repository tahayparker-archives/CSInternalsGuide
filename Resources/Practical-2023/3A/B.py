import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', password='root', database='exam')  # statement 1
if mycon.is_connected():
    print("Successfully connected")
mycursor = mycon.cursor()  # statement 2
mycursor.execute('UPDATE Medicine SET Price=1.1*Price;')  # statement 3
mycon.commit()  # statement 4
mycon.close()