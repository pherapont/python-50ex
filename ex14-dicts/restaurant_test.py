import unittest
from menu import MENU
from restaurant import menu_response

class TestRestaurantMenu(unittest.TestCase):
    def test_dish_on_menu(self):
        self.assertEqual(menu_response('Салат свекольный'), (55, '55'))

    def test_dish_not_on_menu(self):
        self.assertEqual(menu_response('Шампанское'),
                         (0, 'Такого блюда нет в меню.'))
        
if __name__ == '__main__':
    unittest.main()