#/usr/bin/python3
import sqlite3

#Nicolas Mavromatis Nima6629
#Python script to practice db creation and SQL (sqlite3)

#create dbname with four tables
def create(dbname):
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    #Remove tables if they exist to start fresh
    c.execute("DROP TABLE IF EXISTS Store;")
    c.execute("DROP TABLE IF EXISTS Store_Product;")
    c.execute("DROP TABLE IF EXISTS Product;")
    c.execute("DROP TABLE IF EXISTS Category;")
    
    #Create 4 tables
    c.execute("CREATE TABLE IF NOT EXISTS Store(idStore INTEGER PRIMARY KEY, SquareFeet INT, StoreType VARCHAR(45), LocationType CHAR(1), Address VARCHAR(45), City VARCHAR(45), StoreState VARCHAR(45), ZipCode VARCHAR(10));")
    c.execute("CREATE TABLE IF NOT EXISTS Store_Product(ProductID INT, StoreID INT, Quantity INT);")
    c.execute("CREATE TABLE IF NOT EXISTS Product(idProduct INTEGER PRIMARY KEY, Name VARCHAR(30), Price DECIMAL, CategoryID INT, Description VARCHAR(90));")
    c.execute("CREATE TABLE IF NOT EXISTS Category(idCategory INTEGER PRIMARY KEY, Name VARCHAR(45), Description VARCHAR(90));")
    conn.commit()
    conn.close()
    return
    
    #fill tables with sample falues
def fill(dbname):
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    #create arrays to insert values easier
    catArray=[('Food', 'Things you can eat'),
              ('Clothes', 'Things you wear'),
              ('Computers', 'Things that compute')]
    
    storeArray=[(50, 'Grocery Store', 'r', '111 fake ave', 'Cleveland', 'Ohio', '11111'),
               (60, 'Clothes Store', 'r', '222 fake ave', 'Cleveland', 'Ohio', '22222'),
               (70, 'Computer Store', 'o', '333 fake ave', 'Boulder', 'Colorado', '33333')]
    
    
    #Insert values into tables
    c.executemany("INSERT INTO Category(Name, Description) VALUES(?,?)", catArray)
    c.executemany("INSERT INTO Store(SquareFeet, StoreType, LocationType, Address, City, StoreState, ZipCode) VALUES(?,?,?,?,?,?,?)", storeArray)
    #Now manually insert rows into Product, matching CategoryID to Category.rowid
  
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Chicken', 10.50, (SELECT rowid from Category WHERE Category.Name='Food'), 'Fresh Chicken');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Beef', 12.00, (SELECT rowid from Category WHERE Category.Name='Food'), 'Fresh Beef');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Shrimp', 14.00, (SELECT rowid from Category WHERE Category.Name='Food'), 'Fresh Shrimp');")
    
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Shirt', 20, (SELECT rowid from Category WHERE Category.Name='Clothes'), 'Small Shirt');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Jeans', 40, (SELECT rowid from Category WHERE Category.Name='Clothes'), 'Blue Jeans');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Hat', 10, (SELECT rowid from Category WHERE Category.Name='Clothes'), 'Nice Hat');")
    
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Dell Laptop', 100, (SELECT rowid from Category WHERE Category.Name='Computers'), 'Small Laptop');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Keyboard', 20, (SELECT rowid from Category WHERE Category.Name='Computers'), 'Wireless Keyboard');")
    c.execute("INSERT INTO Product(Name, Price, CategoryID, Description) VALUES('Mouse', 10, (SELECT rowid from Category WHERE Category.Name='Computers'), 'Wireless Mouse');")
    
    #Now manually insert rows into Store_Product, matching ProductID and StoreID to respective rowids
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Chicken'), (SELECT idStore FROM Store WHERE Store.StoreType='Grocery Store'), 10);")
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Beef'), (SELECT idStore FROM Store WHERE Store.StoreType='Grocery Store'), 20);") 
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Shrimp'), (SELECT idStore FROM Store WHERE Store.StoreType='Grocery Store'), 30);") 
    
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Shirt'), (SELECT idStore FROM Store WHERE Store.StoreType='Clothes Store'), 50);")
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Jeans'), (SELECT idStore FROM Store WHERE Store.StoreType='Clothes Store'), 52);") 
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Hat'), (SELECT idStore FROM Store WHERE Store.StoreType='Clothes Store'), 54);") 
    
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Dell Laptop'), (SELECT idStore FROM Store WHERE Store.StoreType='Computer Store'), 100);")
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Keyboard'), (SELECT idStore FROM Store WHERE Store.StoreType='Computer Store'), 150);")
    c.execute("INSERT INTO Store_Product(ProductID, StoreID, Quantity) VALUES((SELECT idProduct FROM Product WHERE Product.Name='Mouse'), (SELECT idStore FROM Store WHERE Store.StoreType='Computer Store'), 150);")
 
    conn.commit()
    conn.close()
    
#Function to test table schema is correct (Copied from assignment)
def print_tables(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print ("\nTables:")
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])

     ##   print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        for attr in c.fetchall() :
            print ("\t\t", attr)

        print ("")
        
#Function to test if product to add is valid then add it to Product
def addProduct(dbName, productName, price, categoryID, description):

    #check product name and description are not empty, and are strings
    if((productName=="") or (description=="")):
        raise ValueError
    if((type(productName) is not str) or (type(description) is not str)):
        raise ValueError
    #check price is a float or int and is >=0
    #technically, float is preferred, but user might enter in int
    if ((type(price) is not float) and (type(price) is not int)): 
        raise ValueError
    if (price<0):
        raise ValueError
          
    #check categoryID exists in Category Table, and is an int
    conn=sqlite3.connect(dbName)
    c=conn.cursor()
    
    if(type(categoryID) is not int):
        raise ValueError
    else:
        s="SELECT idCategory FROM Category WHERE idCategory="+str(categoryID)+";"
        c.execute(s)
        obj=c.fetchone()
        #convert rowid to int
        #check if it exists first
        #if none is returned, it means the categoryID does not exist
        if(obj is None):
            raise ValueError
        else:
            idCat=obj[0]
    #Now add item to product. execution will only get this far if it is valid, else it will raise error and exit
    s2="INSERT INTO Product(Name, Price, CategoryID, Description) Values("+"'"+productName+"'"+","+str(price)+","+str(idCat)+","+"'"+description+"'"+");"
    c.execute(s2)
    conn.commit()
    conn.close()
    
