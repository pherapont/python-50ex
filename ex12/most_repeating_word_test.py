import unittest
from most_repeating_word import most_repeating_word_3

class TestMostRepeatingWords(unittest.TestCase):
    '''
    Дана последовательнсть слов.
    1. Надо вернуть слово с наибольшим количеством повторений
    какой-либо буквы.
    2. В случаи одинакового результата у нескольких слов - 
    вернуть любое из них.
    '''
    def test_few_words_with_one_winner(self):
        words = ['this', 'is', 'an', 'elementary',
            'test', 'example']
        win_word = 'elementary'
        self.assertEqual(most_repeating_word_3(words), win_word)

    def test_few_words_with_few_winners(self):
        words = ['apple', 'banana', 'elementary', 'strite']
        wins = ['banana', 'elementary']
        self.assertTrue(most_repeating_word_3(words) in wins)


if __name__ == '__main__':
    unittest.main()
