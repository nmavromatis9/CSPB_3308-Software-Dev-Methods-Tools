import unittest
import os
import sqlite3
import sys

sys.path.append('../Flask/app/')
import routes #Importing routes to test addUser Function


class loginDB_TestCase(unittest.TestCase):
    
    def test_init(self):
        pass
    
    def test_addUser(self):
        with self.assertRaises(ValueError) or self.assertRaises(TypeError):
            myobj = routes.addUser(1, ' ')
            myobj = routes.addUser("abcdefrgb987graptrebnfwegt", ' ') #test length of username
            myobj = routes.addUser("? ", ' ')  #test disallowed symbols
            myobj = routes.addUser("", ' ')   #test empty
            

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()         


    
    
