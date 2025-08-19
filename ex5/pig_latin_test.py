import unittest
from pig_latin import get_pila_word, get_pila_sentence

class TestPigLatin(unittest.TestCase):
    
    def test_one_word_first_vowel(self):
        inp = ['apple', 'orange', 'iris']
        res = ['appleway', 'orangeway', 'irisway']
        for i, word in enumerate(inp):
            self.assertEqual(get_pila_word(word), res[i])

    def test_one_word_first_consonant(self):
        inp = ['cow', 'tiger', 'pyma', 'wolf']
        output = ['owcay', 'igertay', 'ymapay',
            'olfway']
        for i, word in enumerate(inp):
            self.assertEqual(get_pila_word(word), output[i])

    def test_sentence_only_lowercase_words(self):
        inp = 'apple grow on the hill'
        output = 'appleway rowgay onway hetay illhay'
        self.assertEqual(get_pila_sentence(inp), output)

    def test_sentence_with_upper_words(self):
        inp = ['Apple grow on the hill',
            'Little baby drink apple juce']
        output = ['Appleway rowgay onway hetay illhay', 'Ittlelay abybay rinkday appleway ucejay']
        for i, sent in enumerate(inp):
            self.assertEqual(get_pila_sentence(sent), output[i])

if __name__ == '__main__':
    unittest.main()
