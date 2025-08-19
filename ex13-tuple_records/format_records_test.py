'''
def format_records 
на вход: список кортежей
на выход: форматированная строка
отсортированная по первому полю
Требования:
    1. Фамилия перед именем
    2. каждое имя в поле 10 символов
    3. время в поле 5 символов
    4. время - число с 2 цифрами после десятичной точки
        (10.603 -> 10.60)
'''

from format_records import format_records
from format_records_test_data import PEOPLE, OUTPUT_LINE
import unittest

class TestFormatRecords(unittest.TestCase):
    def test_format_records(self):
        self.assertEqual(format_records(PEOPLE) ,OUTPUT_LINE)

if __name__ == '__main__':
    unittest.main()