import unittest
from strsort import strsort

class StringSortingTest(unittest.TestCase):
    def test_sort_lowercase_string_uniqe(self):
        '''
        Sorting string whithout witerspace with uniques letters
        '''
        inp = ['bca', 'orange',]
        output = ['abc', 'aegnor']
        for i, o in zip(inp, output):
            self.assertEqual(strsort(i), o, msg='Eoh')

if __name__ == '__main__':
    unittest.main()
