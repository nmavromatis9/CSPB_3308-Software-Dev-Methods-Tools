import unittest
import os
import sqlite3
import sys

sys.path.append('../Flask/app/')
import routes #Importing routes to test addUser Function


class loginDB_TestCase(unittest.TestCase):
    
    def test_init(self):
        pass
    
    def test_addUserName(self):
        with self.assertRaises(ValueError) or self.assertRaises(TypeError):
            myobj = routes.addUser(1, ' ')
            myobj = routes.addUser("abcdefrgb987graptrebnfwegt", ' ') #test length of username
            myobj = routes.addUser("? ", ' ')  #test disallowed symbols
            myobj = routes.addUser("", ' ')   #test empty
    
    def test_addUserPW(self):
        with self.assertRaises(ValueError) or self.assertRaises(TypeError):
            myobj = routes.addUser("CharlesNorris", 1)
            myobj = routes.addUser("CharlieNorris", "") #test length of password
            myobj = routes.addUser("ChuckyNorris", "?")  #test disallowed symbols
            myobj = routes.addUser("Walker", "")   #test empty
    
    def test_insertHospitalDBCount(self):
        try:
            con = sqlite3.connect("DB_Setup/hospital.db")
            cur=con.cursor()
        except:
            print("BAD CONNECTION")
        cur.execute("Select Count(*) from tblInsurer")
        c1 = cur.fetchone()
        cur.execute("INSERT INTO tblInsurer VALUES (7001, 7001, 'Roundhouse', 'We kick the costs') ")
        cur.execute("Select Count(*) from tblInsurer")
        c2 = cur.fetchone()
        self.assertEqual(c2[0], c1[0] + 1)
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()         


    
    
