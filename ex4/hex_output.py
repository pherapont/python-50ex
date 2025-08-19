'''
    Модуль для преобразования шестнадцетеричного числа
    в десятичное
'''

def hex_output(hex_str):
    '''
    param hex_str: str - шестнадцетеричное число в строковом
        представлении
    return : int - десятеричное преобразование введеного числа
    '''

    res = 0

    for index, digit in enumerate(reversed(hex_str)):
        if not digit in '0123456789abcdefABCDEF':
            raise HexStringError('Некорректный ввод для шестнадцетиричного числа')
        res += int(digit, 16) * 16 ** index

    return res

class HexStringError(ValueError):
    '''
    Исключение при получении некорректного ввода шестнадцетеричного
    числа
    '''
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"HexStringError: {self.message}"


def main():
    inp = input('Введите шестнадцетеричное число: ')
    try:
        res = hex_output(inp)
        print(f"Результат преобразования в десятичное число: {res}")
    except HexStringError:
        print("Вы ввели неправилные данные")

if __name__ == '__main__':
    main()
