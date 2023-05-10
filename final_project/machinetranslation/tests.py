import unittest

from translator import englishToFrench , frenchToEnglish

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        self.assertNotEqual(englishToFrench('Hello'), 'Hello') 
class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour') 
       
unittest.main()