'''
Идея по тестированию функции get_final_line: создаем тестовый файл,
записываем в него несколько строк, потом применяем к нему get_final_line,
и в результате должны получить последнюю строку.
'''
import unittest
from last_line import get_final_line

strings = [
    'My little friend.',
    'I want to send your',
    'it little present.',
    "I'm go back",
    ]

test_file = 'test_lines.txt'


class TestGetFinalLine(unittest.TestCase):

    def test_get_final_line(self):
        with open(test_file, 'w') as tf:
            for line in strings:
                tf.write(line)
                tf.write('\n')
        self.assertEqual("I'm go back\n", get_final_line(test_file))

    def test_final_line_this_file(self):
        self.assertEqual(get_final_line("last_line_test.py"),
                         "    unittest.main()\n")


if __name__ == '__main__':
        unittest.main()
