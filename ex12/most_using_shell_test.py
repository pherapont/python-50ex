import unittest
from most_using_shell import read_shell_file

class TestMostUsingShell(unittest.TestCase):
    def test_has_docstring(self):
        self.assertFalse(read_shell_file.__doc__ == None, 
                "It's nessesary add docstring to function")

    def test_read_shell_file_output(self):
        shpath = 'test_data_shell.txt'
        res = {'bash': ['root', 'kon'], 
            'nologin': ['daemon', 'bin', 'sssd'],
            'false': ['mysql']
        }
        self.assertEqual(read_shell_file(shpath), res,
            'Неправильное форматирование данных, полученных из файла')

if __name__ == '__main__':
    unittest.main()
