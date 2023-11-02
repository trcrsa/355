import unittest
from example import sumOf

class Cases(unittest.TestCase):
    def test_neg(self):
        result = sumOf(-1,-1)
        self.assertEqual(result, -2)



