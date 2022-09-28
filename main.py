import mysql.connector
from func import dbpass,dbuser,dbhost,shell,lstprint,dbcheck,tablecheck,loadstock,prettytables,cartadd,altshell,addsale,adminpass,loadsales,addvendor
#load mysql connection details from .env 
user = str(dbuser())
host = str(dbhost())
pwd = str(dbpass())
#Open mysql connection and check db exists
intdb = mysql.connector.connect(
    host=host,
    user=user,
    password=pwd,
)
print(dbcheck(intdb))
intdb.close()
#Open mysql connection and check table exists
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=pwd,
    database="electonics"
)
print(tablecheck(mydb))
mydb.close()
db = mysql.connector.connect(
    host=host,
    user=user,
    password=pwd,
    database="electonics"
)
#lstprint(shell(db,input(">")))
#print(shell(mydb,input(">")))
print("Welcome to the pear electonic store")
admin=input("Do you want to purchase something? ")
if admin in ["yes",'y']:
    buy=True
elif admin =="no":
    buy=False
else:
    print("Invalid Input")
cart=[]
while buy==True:
    print("Select the items you would like to purchase, Enter its ID")
    #Load stock
    print("| ID | VENDOR | BRAND | UNITS | MODEL |")
    prettytables(loadstock())
    x=int(input(">"))
    cartadd(x,cart)
    print(cart)
    admin=input("Do you want to purchase another item? ")
    if admin in ["yes",'y']:
        buy=True
    elif admin =="no":
        buy=False
    else:
        print("Invalid Input")
        buy=False
if cart!=[]:
    print("Please enter your information to complete your purchase")
    pno=input("Enter your phone number: ")
    pname=input("Enter your First and Last name: ")
    paddress=input("Enter your address: ")
    addsale(pname,paddress,pno)
if admin=="no":
    if input("Enter pass:> ") == adminpass():
        while admin=="no":
            print("Hello admin")
            print("| ID | NAME | ADDRESS | PHONE |")
            prettytables((loadsales()))
            f =input("add more vendors and stock data? ")
            if f in ["yes","y"]:
                print("| ID | VENDOR | BRAND | UNITS | MODEL |")
                prettytables(loadstock())
                vendor=input("Enter vendor name: ")
                brand=input("Enter product brand: ")
                units=input("Enter number of units of product: ")
                model=input("Enter model of product: ")
                addvendor(vendor,brand,units,model)
            elif f in ["no","n"]:
                admin="bye"
            else:
                print("invalid input")
                admin="bye"
db.commit()
