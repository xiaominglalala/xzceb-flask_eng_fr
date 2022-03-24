import unittest
from translator import frenchToEnglish, englishToFrench

class Testf2e(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frenchToEnglish('1'), '1')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class Teste2f(unittest.TestCase):
    def test_1(self):
        self.assertEqual(englishToFrench('2'), '2')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

unittest.main()
