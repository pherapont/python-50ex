import random

def guessing_game():
    num = random.randint(1, 100)
    print(num)

    while (ans := user_input()) != num:
        print(ans)
        if ans > num:
            print('Число слишком большое')
        else:
            print('Число слишком маленькое')
    print('В самый раз')

def user_input():
    return int(input('Введите число от 1 до 100: '))

if __name__ == '__main__':
    guessing_game()
