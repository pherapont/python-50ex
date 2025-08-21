'''
1. Модуль запрашивает ввод блюда заказа у пользователя.
2. Проверка наличия блюда в меню
3. Показать пользователю цену блюда и общую сумму заказа
4. Если блюда нет в меню изивиниться и предложить продолжить
5. Окончание по вводу пустой строки
'''

from menu import MENU

def menu_response(req: str) -> tuple[int, str]:
    price = MENU[req] if req in MENU else 0
    ans = str(price) if price else 'Такого блюда нет в меню.'
    return (price, ans)  

def user_communication():
    sum = 0
    while order := input('Заказ: ').strip():
        resp = menu_response(order)
        sum += resp[0]
        if resp[0]:
            print(f"{order} стоит {resp[0]}, общая сумма {sum}")
        else:
            print(resp[1], order)
    print('Общая сумма:', sum)
    print('Спасибо за заказ!')

if __name__ == '__main__':
    user_communication()
            
