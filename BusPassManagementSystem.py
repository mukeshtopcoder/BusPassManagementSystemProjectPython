# BUS PASS MANAGEMENT SYSTEM PROJECT

# Database Connection
import mysql.connector
conn = mysql.connector.connect(
host = "127.0.0.1",
user = "root",
passwd = "553655",
database = "bus"
    )
# Create A Cursor
cur = conn.cursor()

# Method to create a Pass
def createPass():
    try:
        name = input("Enter New User Name : ")
        sql = "INSERT INTO users(uname) VALUE(%s)"
        data = tuple([name])
        cur.execute(sql,data)
        conn.commit()
        print("Pass Create Successfully!")
    except Exception as e:
        print("Error :",e)

# Method to Check Balance of A Pass
def checkBalance():
    try:
        idd = input("\n\nEnter User ID : ")
        sql = "SELECT * FROM users WHERE id="+idd
        cur.execute(sql)
        result = cur.fetchall()
        if(len(result)!=0):
            for user in result:
                print("User ID :",user[0])
                print("User Name :",user[1])
                print("Pass Balance :",user[2])
        else:
            print("Pass Not Available!")       
    except Exception as e:
        print("Error :",e)

# Method to Reacharge A Pass
def recharge():
    try:
        idd = input("\n\nEnter User ID : ")
        sql = "SELECT * FROM users WHERE id="+idd
        cur.execute(sql)
        result = cur.fetchall()
        if(len(result)!=0):
            balance = int(input("Enter Balance : "))
            sql = "SELECT balance FROM users WHERE id="+idd
            cur.execute(sql)
            result = cur.fetchall()
            for bal in result:
                balance = int(bal[0])+balance
            sql = "UPDATE users SET balance="+str(balance)+" WHERE id="+idd
            cur.execute(sql)
            conn.commit()
            print("Pass Recharged Successfully!")
        else:
            print("User Not Found!\n")
    except Exception as e:
        print("Error :",e)

# Method to Charge A Fare Based on KiloMeters
def chargeFare():
    try:
        idd = input("\n\nEnter User ID : ")
        sql = "SELECT * FROM users WHERE id="+idd
        cur.execute(sql)
        result = cur.fetchall()
        if(len(result)!=0):
            for bal in result:
                print("Name :",bal[1])
                print("Balance :",bal[2])
                dis = int(input("\nEnter Distance in KM : "))
                fare = dis*15
                print("Your Fare is :",fare)
                sql = "SELECT balance FROM users WHERE id="+idd
                cur.execute(sql)
                result = cur.fetchall()
                for bal in result:
                    if(fare<=int(bal[0])):
                        balance = int(bal[0])-fare
                        sql = "UPDATE users SET balance="+str(balance)+" WHERE id="+idd
                        cur.execute(sql)
                        conn.commit()
                        print("Fare Has Deducted Successfully!")
                    else:
                        print("Insufficient Balance!")
        else:
            print("User Not Found!")
    except Exception as e:
        print("Error :",e)

# Method to View All Pass Users
def viewAllPass():
    try:
        sql = "SELECT * FROM users"
        cur.execute(sql)
        result = cur.fetchall()
        for u in result:
            print("ID : ",u[0])
            print("Name : ",u[1])
            print("Balance : ",u[2])
            print("\n*******************\n")
    except Exception as e:
        print("Error :",e)

# Dashboard of Bus Pass Management System
ch = 'a'
while(True):
    print("\n\n******* BUS PASS MANAGEMENT SOFTWARE *******\n")
    print("1. Create Pass")
    print("2. Check Balance of Pass")
    print("3. Recharge A Pass")
    print("4. Charge Fare")
    print("5. View All Pass Users")
    print("6. Exit\n")
    ch = input("Enter Your Choice : ")
    if(ch=='6'):
        print("Bye-Bye")
        break
    elif(ch=='1'):
        createPass()
    elif(ch=='2'):
        checkBalance()
    elif(ch=='3'):
        recharge()
    elif(ch=='4'):
        chargeFare()
    elif(ch=='5'):
        viewAllPass()
    else:
        print("Wrong Entered! Try Again!")
