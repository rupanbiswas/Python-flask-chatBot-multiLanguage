import unittest

from translator import englishToFrench , frenchToEnglish

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
       
unittest.main()