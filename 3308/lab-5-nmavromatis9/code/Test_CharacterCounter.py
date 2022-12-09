#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler, David Knox
# Summer 2014, 2022
# CSCI 3308
# Univerity of Colorado
# Tests for Character Counting Module

import unittest
from CharacterCounter import *

class CharCounterTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

  
    def test_init(self):
        text = "tesing123"
        
        # create an object that we will use in this testing
        p = CharacterCounter(text)
        
        # use the testing framework assertions to check results
        self.assertEqual(p.text, text, "'text' does not match input")
        
        # need to test that an exception is raised when given a bad parameter!
        # any other tests?
        
    # Add Your Test Cases Here...
    
    #Test verifies the constructor raises an error if passed something other than a string
    #Pass all known python types other than string
    def test_string(self):
        tests = [
            [1],
            [1.0],
            [True],
            [[1, 2, 3]],
            [b"Hello"],
            [1.8e308],
            [2+3j],
            [("apple", "orange", "watermelon")],
            [range(6)],
            [{"name" : "Mike", "age" : 38}],
            [{"saw", "hammer", "nail"}],
            [frozenset({"apple", "orange", "watermelon"})],
            [bytearray(5)],
            [memoryview(bytes(5))],
            [None]
            
        ]
        
        for test in tests:
            # check that an exception is raised. 
            #Test only fails if CharacterCounterError exception is NOT raised
            with self.assertRaises(CharacterCounterError):
                # create a new object for each test, which uses __init__(), and should throw exception
                my_obj = CharacterCounter(test[0])
            
            
            
    # here is an example way to write tests.  You can do it other ways as well.
    # THIS IS NOT A GOOD SET OF TESTS, JUST AN EXAMPLE
    #
    #I changed this function. Should count number of alpha characters
    def test_alpha(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["aaaa", 4, "did not find all occurrences of single char"],
            ["a        b", 2, "did not find first and last character of string"],
            ["az", 2, "did not detect a and/or z"],
            ["(a1)", 1, "did not detect handle string with alpha, digit, paren" ],
            ["1239093", 0, "found alpha in digits only string"],
            ["", 0, "did not count empty string as zero"],
            ["`~!@#$%^&*{}[](),./?:;'\|<>-_+=", 0, "did not count punctuation/unique chars correctly"],
            ["A", 1, "did not count capital char"],
            ["A    Z", 2, "did not count capital chars with spaces"],
            #I added tests to test all alpha characters
            ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 52, "Did not count all alpha characters."],
            #Added test to test all digit characters
            ["0123456789", 0, "Counted digits incorrectly"]
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.count_alpha(), test[1], test[2])
    
    #test the count() method, returns num of chars in string
    def test_count(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["aaaa", 4, "did not count string with only one char type"],
            ["a", 1, "did not count string with only one char total"],
            ["a        b", 10, "did not count spaces"],
            ["qwer_ty", 7, "did not count underline"], 
            ["`~!@#$%^&*{}[](),./?:;'\|<>-_+=", 31, "did not count punctuation/unique chars"],
            ["test", 4, "did not count normal string chars" ],
            ["1239093", 7, "did not count numbers in string"],
            ["", 0, "did not count empty string"],
            ["\"", 1, "did not count \" "]
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.count(), test[1], test[2])
            
    # add methods for other functions that need to be tested ...
    
    #test count_numeric()
    def test_numeric(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["1234", 4, "did not count basic number"],
            ["1111", 4, "did not count repeated digit"],
            ["1        2", 2, "did not find first and last character of string"],
            ["abcdefg", 0, "did not count 0 correctly in alpha string"],
            ["`~!@#$%^&*{}[](),./?:;'\|<>-_+=", 0, "incorrectly counted punctuation/unique chars"],
            ["", 0, "did not count empty string as zero"],
            ["1234.5", 5, "did not count digits with decimal"],
            ["1  4  2", 3, "did not count digits with spaces"],
            ["0", 1, "did not count 0"],
            ["1234567890", 10, "did not count all digits"],
            #Added test for all alpha characters
            ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, "Incorrectly counted alpha characters."]
            
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.count_numeric(), test[1], test[2])
            
    #test count_vowels()
    def test_vowels(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["aeou", 4, "did not count lowercase vowels"],
            ["aaaaa", 5, "did not count repeated vowel"],
            ["AEOU", 4, "did not count uppercase vowels"],
            ["a        u", 2, "did not find first and last vowel of string"],
            ["abcdefg", 2, "did not count vowels correctly in alpha string"],
            ["`~!@#$%^&*{}[](),./?:;'\|<>-_+=", 0, "incorrectly counted punctuation/unique chars"],
            ["", 0, "did not count empty string as zero"],
            ["123u4.5", 1, "did not count vowel in number"],
            ["a  o  u", 3, "did not count vowels with spaces"],
            ["i", 1, "did not count i"],
            ["I", 1, "did not count I"],
            ["aeiouAEIOU", 10, "did not count all vowels (upper and lower case)"],
            #Added test for all alpha characters
            ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 10, "Incorrectly counted non-vowel alpha characters."],
            #Added test for all digit characters
            ["0123456789", 0, "Incorrectly counted digits."]
            
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.count_vowels(), test[1], test[2])
            
            #test is_phonenumber()
    def test_phonenumber(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["123..123..123", False, "Did not ret False for nine digit number with too many . delimiters"],
            ["123..123..1234", False, "Did not ret True for 10 digit number with correct too many . delimiters"],
            ["123--123--123", False, "Did not ret False for nine digit number with too many - delimiters"],
            ["123--123--1234", False, "Did not ret False for 10 digit number with too many - delimiters"],
            ["123.123.123", False, "Did not ret False for nine digit number with correct . delimiters"],
            ["123.123.1234", True, "Did not ret True for 10 digit number with correct . delimiters"],
            ["123.123-123", False, "Did not ret False for nine digit number with mixed delimiters"],
            ["123.123-1234", False, "Did not ret True for 10 digit number with mixed delimiters"],
            ["123-123-123", False, "Did not ret False for nine digit number with correct - delimiters"],
            ["123-123-1234", True, "Did not ret True for 10 digit number with correct - delimiters"],
            ["123123123", False, "Did not ret False for nine digit number with no delimiters"],
            ["1231231234", True, "Did not ret True for ten digit number with no delimiters"],
            ["123-123-123", False, "Did not ret False for 9 digit number"],
            ["123-123-1234", True, "Did not ret True for 10 digit number"],
            ["1234", False, "did not ret false for regular number"],
            ["1        2", False, "did not ret False for number with space"],
            ["abcdefg", False, "did not ret false for alpha string"],
            ["`~!@#$%^&*{}[](),./?:;'\|<>-_+=", False, "did not ret false for special chars"],
            ["", False, "did not ret False for empty string"],
            ["1234.5", False, "did not ret False for decimal number"],
            ["1  4  2", False, "did not ret False for spaced number"],
            ["12345678901", False, "did not ret False for 11 digit number"],
            ["1234567890", True, "did not ret True for correct 10 digit number"],
            ["13.123.123", False, "Did not ret False for 8 digit number with correct . delimiters"],
            ["012.123.123", False, "Did not ret False for 9 digit number with 0 as first digit"],
            ["012.123.1234", False, "Did not ret False for 10 digit number with 0 as first digit"],
            ["123.023.1234", True, "Did not ret True for 10 digit number with correct 0 in pos 2"],
            ["123.123.0234", True, "Did not ret True for 10 digit number with correct 0 in pos 3"],
            ["123.123.1034", True, "Did not ret True for 10 digit number with correct 0 in pos 4"],
            ["567.843.2061", True, "Did not ret True for 10 digit number with mix of digits"],
            ["567.843..2061", False, "Did not ret False for 10 digit number with .. in second pos"],
            ["112345678901", False, "did not ret False for 12 digit number"],
            ["(567)8432061", True, "Did not ret True for 10 digit number with ()"],
            ["(567)843-2061", True, "Did not ret True for 10 digit number with () and - in second pos"],
            ["(567)843.2061", True, "Did not ret True for 10 digit number with () and . in second pos"],
            ["(567)-843-2061", False, "Did not ret False for 10 digit number with () and - in first pos"],
            ["1(567)843.2061", False, "Did not ret False for 11 digit number with () and . in second pos"]
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.is_phonenumber(), test[1], test[2])
            
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
