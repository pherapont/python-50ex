import unittest
from hex_output import hex_output, HexStringError 

class TestHexOutput(unittest.TestCase):
    
    def test_input_only_numbers(self):
        '''
        Функция принимает на вход шестнадцетеричное число
        в виде строки десятичных чисел и возвращает int
        '''
        
        res = hex_output('50')
        self.assertEqual(res, 80)

    def test_input_number_and_letter(self):
        '''
        Функция принимает на вход строку с цифрами и буквами
        a, b, c, d, e, f в разных регистрах (соответствуют
        шестнадцетиричному числу). 
        Возвращает int.
        '''
        res = hex_output('ff')
        self.assertEqual(res, 255)

    def test_exception_to_wrong_input(self):
        '''
        Функция генерирует специальное исключение при неправильном
        аргументе
        '''

        with self.assertRaises(HexStringError):
            hex_output('asd')

if __name__ == '__main__':
    unittest.main()
