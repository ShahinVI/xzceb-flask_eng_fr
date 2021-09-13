'''
this code is to test the file translator
'''
import unittest #importing testing tools
from translator import english_to_french, french_to_english
#importing functions to be tested

class TestE2F(unittest.TestCase):
    def test1(self):
        '''
        test the function to translate from English
        to French
        '''
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestF2E(unittest.TestCase):
    def test2(self):
        '''
        test the function to translate from French
        to English
        '''
        self.assertEqual(french_to_english(' '),' ')
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
