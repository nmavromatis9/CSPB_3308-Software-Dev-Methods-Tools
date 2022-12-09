#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Nicolas Mavromatis (nima6629)
#Script to test SQL code of storedb.py

import unittest
import os
from storedb import *

class DataBaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #Make two calls to storedb.py to be ready for tests
    def setUp(self):
        create('test.db')
        fill('test.db')
        return 
    
    def tearDown(self):
        os.remove('test.db')
        return 
    
    #Test SQL Queries return correct Tuple, then test single value
    def test_category(self):
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("SELECT * FROM CATEGORY WHERE idCategory=1;")
        obj1=c.fetchone()
        self.assertEqual(obj1, (1, 'Food', 'Things you can eat'), "First row of Category is not as expected.")
        
        c.execute("SELECT Description FROM CATEGORY WHERE Name='Clothes'")
        obj2=c.fetchone()
        self.assertEqual(obj2, ("Things you wear",), "Second row of Category not as expected")
        conn.commit()
        conn.close()
        
    def test_store(self):
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("SELECT * FROM STORE WHERE Address='222 fake ave';")
        obj=c.fetchone()
        self.assertEqual(obj, (2, 60, 'Clothes Store', 'r', '222 fake ave', 'Cleveland', 'Ohio', '22222'), "Second row of Store not as expected.")
        
        c.execute("SELECT StoreState FROM Store WHERE idStore=3;")
        obj2=c.fetchone()
        self.assertEqual(obj2, ("Colorado",), "Row 3 of Store not as expected")
        conn.commit()
        conn.close()
        
    def test_product(self):
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Product WHERE Name='Candy';")
        obj=c.fetchone()
        #This test should return none
        self.assertEqual(obj, None, "Return was not None as Expected")
        
        c.execute("SELECT * FROM Product WHERE Description='Fresh Shrimp';")
        obj2=c.fetchone()
        self.assertEqual(obj2, (3, 'Shrimp', 14, 1, 'Fresh Shrimp'), "Row 3 of Product not as expected")
        conn.commit()
        conn.close()
        
    def test_store_product(self):
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Product WHERE Quantity=100;")
        obj=c.fetchone()
        self.assertEqual(obj, (7, 3, 100), "Row 7 of Store_Product not as expected")
        
        c.execute("SELECT Quantity FROM Store_Product WHERE ProductID=8;")
        obj2=c.fetchone()
        self.assertEqual(obj2, (150,), "Row 8 of Store_Product not as expected")
        conn.commit()
        conn.close()
        
#########################################
#addProduct(dbName, productName, price, categoryID, description) tests
    
    #addProduct should raise a ValueError if name or description are empty or not strings.
    def test_empty(self):
        #Test empty description and name
        with self.assertRaises(ValueError):
            test1=addProduct("test.db", "Fish", 700, 1, "")
        with self.assertRaises(ValueError):
            test2=addProduct("test.db", "", 800, 3, "Empty String Description")
        with self.assertRaises(ValueError):
            test3=addProduct("test.db", "", 800, 3, "")    
        #Test one or both not strings
        with self.assertRaises(ValueError):
            test3=addProduct("test.db", 50, 800, 3, "Description") 
        with self.assertRaises(ValueError):
            test3=addProduct("test.db", "Fish", 800, 3, 20) 
        with self.assertRaises(ValueError):
            test3=addProduct("test.db", 50, 800, 3, 20) 
            
    #addProduct should raise a ValueError if price is less than 0 or not a number.    
    def test_price(self):
        with self.assertRaises(ValueError):
            test1=addProduct("test.db", "Fish", -1.0, 1, "Description")
        with self.assertRaises(ValueError):
            test2=addProduct("test.db", "Fish", "Not A Number", 1, "Description")
            
    #addProduct should raise a ValueError if categoryID is not a valid rowid in the category table.
    def test_categoryID(self):
        #try a negative categoryID
        with self.assertRaises(ValueError):
            test1=addProduct("test.db", "Fish", 800.0, -10, "Fresh Fish")
        #Try a categoryID not an int
        with self.assertRaises(ValueError):
            test1=addProduct("test.db", "Fish", 700, "String", "Description")
        #Try a categoryID too big to exist in this example
        with self.assertRaises(ValueError):
            test1=addProduct("test.db", "Fish", 700, 1000, "Description")
            
    #if addProduct returns successfully, the product table should have a new row in it with the correct information
    def test_successful(self):
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("SELECT rowid from Category WHERE Category.Name='Food';")
        catID=c.fetchone()
        #extract int from tuple
        i=catID[0]
        test1=addProduct("test.db", "Fish", 700, i, "Fresh Fish")
        c.execute("SELECT * FROM Product WHERE Name='Fish';")
        obj2=c.fetchone()
        self.assertEqual(obj2, (10, 'Fish', 700, i, 'Fresh Fish'), "AddProduct could not add valid product")
        
        
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()