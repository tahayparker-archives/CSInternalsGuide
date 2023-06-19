import pickle
L = []


def Add():
    f = open("store.dat", "wb")
    n = int(input("Enter quantity of phones: "))
    
    for i in range(n):
        no = input("Enter phone number: ")
        name = input("Enter phone name: ")
        company = input("Enter phone company: ")
        price = input("Enter phone price: ")
        L.append([no, name, company, price])
    pickle.dump(L, f)
    f.close()


def Display():
    f = open("store.dat", "rb")
    try:
        c = pickle.load(f)
        for i in c:
            print("Phone Number: ", i[0], "\tPhone Name: ", i[1], "\tCompany: ", i[2], "\tPrice: ", i[3], "\n")
    except EOFError:
        f.close()


def Count_Item(Item):
    f = open("store.dat", "rb")
    try:
        c = pickle.load(f)
        count = 0
        for i in c:
            if i[2] == Item:
                count += 1
        print("Total number of ", Item, " is ", count)
    except EOFError:
        f.close()


while True:
    print("Menu")
    print("1. Add\n2. Display\n3. Count Item\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Add()
    elif ch == 2:
        Display()
    elif ch == 3:
        Item = input("Enter item to count: ")
        Count_Item(Item)
    elif ch == 4:
        exit()