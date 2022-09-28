import csv,mysql.connector
from mysql.connector import errorcode
#Grabs dbpass from .env
def dbpass():
    fh = open(".env","r")
    reader = csv.reader(fh)
    for i in reader:
        if i[0] == "pass":
            return i[1]
#Grabs dbuser from .env
def dbuser():
    fh = open(".env","r")
    reader = csv.reader(fh)
    for i in reader:
        if i[0] == "user":
            return i[1]
#Grabs dbhost from .env
def dbhost():
    fh = open(".env","r")
    reader = csv.reader(fh)
    for i in reader:
        if i[0] == "host":
            return i[1]
#Grabs adminpass from .env
def adminpass():
    fh = open(".env","r")
    reader = csv.reader(fh)
    for i in reader:
        if i[0] == "admin":
            return i[1]
#Mysql.execute with error handling
def shell(inp):
    user = str(dbuser())
    host = str(dbhost())
    pwd = str(dbpass())
    udb = mysql.connector.connect(host=host,user=user,password=pwd,database="electonics")
    cursor=udb.cursor()
    try:
        cursor.execute(inp)
        out = []
        for x in cursor:
            out.append(x)
        udb.commit()
        udb.close()
        return out
    except mysql.connector.Error as err:
        if err.errno == 1064:
            print("Check your syntax!")
        if err.errno == 1007:
            return(True)
        if err.errno == 1050:
            return(True)
        else:
            return ("Error: {}".format(err))
            #print("Error: {}".format(err))
    udb.commit()
    udb.close()
#Prints all items in list
def lstprint(inp):
    if type(inp) is list:
        for i in inp :
            print(i)
    else:
        print("Not a list")
#Checks if all tables exist and if not creates them
def altshell(db,inp):
    cursor=db.cursor()
    try:
        cursor.execute(inp)
        out = []
        for x in cursor:
            out.append(x)
        return out
    except mysql.connector.Error as err:
        if err.errno == 1064:
            print("Check your syntax!")
        if err.errno == 1007:
            return(True)
        if err.errno == 1050:
            return(True)
        else:
            return ("Error: {}".format(err))
            #print("Error: {}".format(err)) prints Error: {ErrorCode}
def dbcheck(mydb):
    a = altshell(mydb,"CREATE DATABASE electonics")
    altshell(mydb,"SHOW DATABASES")
    if a == 0:
        return("Database was created")
    else:
        return("Database already exists")
def tablecheck(mydb):
    check = []
    checked = None
    #Check stock table
    check.append(altshell(mydb,"CREATE TABLE stock ( id INT, vendor varchar(255), brand varchar(255), units varchar(255), model varchar(255));"))
    #Check vendor data table
    #check.append(altshell(mydb,"CREATE TABLE vendor_data ( vendor_name varchar(255), vendor_brands varchar(255));  "))
    #Check sales table
    check.append(altshell(mydb,"CREATE TABLE sales ( id INT(255), name varchar(255), address varchar(255), phone BIGINT);"))
    #Returns to user if databases were created
    for i in check:
        if i == True: checked=1
        else: checked=0
    if checked == 0:
        return("All/Some Tables were created")
    else:
        return("All tables exist already")
#Load stock
def loadstock():
    return shell("SELECT * FROM stock;")
#Load sales
def loadsales():
    return shell("SELECT * FROM sales;")
# Pretty tables
def prettytables(table):
    for i in table:
        l = list(i)
        string=""
        for i in l:
            string=string+str(i)+" | "
        print("| " + string)
#add to cart 
def cartadd(id,cart):
    exc="SELECT units FROM stock WHERE id=" + str(id)+";"
    out=shell(exc)
    out = int(out[0][0])
    if out>0:
        cart.append(id)
        shell("UPDATE stock SET units="+str(out-1)+" WHERE id="+str(id)+";")
    else:
        print("Out of stock")
#add record to sales 
def addsale(name,addr,phone):
    x=shell("SELECT id FROM sales;")
    y=list(x[-1])
    y.sort()
    id=y[-1]+1
    shell("INSERT INTO sales VALUES ("+str(id)+",'"+name+"','"+addr+"',"+phone+");")
#add record to vendor
def addvendor(vendor,brand,units,model):
    x=shell("SELECT id FROM stock;")
    y=list(x[-1])
    y.sort()
    id=y[-1]+1
    print(x,id)
    shell("INSERT INTO stock VALUES ("+str(id)+",'"+vendor+"','"+brand+"','"+str(units)+"','"+model+"');")
    print("INSERT INTO stock VALUES ("+str(id)+",'"+vendor+"','"+brand+"','"+str(units)+"','"+model+"');")
