'''
Функция alphabetize_names получает на вход список словарей
{first:, last:, email:} и возвращает список этих словарей, 
отсортированных по first and last
'''
import unittest
from names_data import PEOPLE as PEOPLE_INPUT
from alphabetize_names_test_data import PEOPLE as PEOPLE_OUTPUT
from alphabetize_names import alphabetize_names_0, alphabetize_names_1

class TestAlphabetizeNames(unittest.TestCase):
    def test_convert_dict(self):
        self.assertEqual(alphabetize_names_1(PEOPLE_INPUT), PEOPLE_OUTPUT)

if __name__ == '__main__':
    unittest.main()
