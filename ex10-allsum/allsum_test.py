import unittest
from allsum import allsum

class TestAllSum(unittest.TestCase):
    def test_no_arguments(self):
        with self.assertRaises(ValueError):
            allsum()

    def test_sum_ints(self):
        data = (1, 2, 3, 4, 5, 6)
        res = 21
        self.assertEqual(allsum(*data), res)

    def test_sum_floats(self):
        data = (0.1, 0.9, 1.5, 10.6)
        res = 13.1
        self.assertEqual(allsum(*data), res)
        
    def test_sum_tuples(self):
        data = [(0, 1), (2, 3), (4, 5), (6, 7)]
        res = (0, 1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(allsum(*data), res)

    def test_sum_lists(self):
        data = [[0, 1], [2, 3], [4, 5], [6, 7]]
        res = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(allsum(*data), res)

    def test_sum_strings(self):
        data = ('Hello', ',', ' ', 'world', '!')
        res = 'Hello, world!'
        self.assertEqual(allsum(*data), res)

if __name__ == '__main__':
    unittest.main()
