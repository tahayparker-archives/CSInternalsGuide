import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', password='root', database='exam')  # statement 1
if mycon.is_connected():
    print("Successfully connected")
mycursor = mycon.cursor() # statement 2
mycursor.execute('UPDATE Customer SET City="Chennai" WHERE CustomerID = 134')  # statement 3
mycon.commit()  # statement 4
mycon.close()