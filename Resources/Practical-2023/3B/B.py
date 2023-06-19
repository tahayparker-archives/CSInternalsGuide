import mysql.connector  # 1
mycon = mysql.connector.connect(host="localhost", user="root", password="root", database="exam")
if mycon.is_connected():
    print("Successfully connected")
mycursor = mycon.cursor()  # 2


def display():
    mycursor.execute("SELECT * FROM Stationery WHERE Price > 10;")  # statement 3
    data = mycursor.fetchall()
    for row in data:
        print(row)
    mycon.close()


display()