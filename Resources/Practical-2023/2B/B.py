import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', password='root', database='exam')  # statement 1
if mycon.is_connected():
    print("Successfully connected")
mycursor = mycon.cursor()  # statement 2
mycursor.execute('ALTER TABLE Games ADD No_of_participants INT NOT NULL;')  # statement 3
mycon.commit()  # statement 4
mycon.close()