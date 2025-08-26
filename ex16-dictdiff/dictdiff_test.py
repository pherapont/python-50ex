import unittest
from dictdiff import dictdiff

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'd':3}

class TestDictDiff(unittest.TestCase):
    
    def test_equal_dicts(self):
        self.assertEqual(dictdiff(d1, d1), {})

    def test_diff_only_in_value(self):
        self.assertEqual(dictdiff(d1, d2), {'c': [3, 4]})

    def test_diff_only_keys(self):
        self.assertEqual(dictdiff(d2, d4), {'c': [4, None],
            'd': [None, 3]})
