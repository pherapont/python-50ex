'''
Модуль реализует метод шифрования текста - поросячья латынь
'''

VOWELS = ['a', 'e', 'i', 'o', 'u']

def get_pila_word(word: str)-> str:
    '''
    Шифруем поросячей латынью одно слово
    Метод шифрования:
        если первая буква - гласная: в конце слова добавляем 'way',
        если первая буква - согласная: первую букву переносим в 
            конец слова и добавляеи 'ay'
    '''
    flag = False

    if word[0].isupper():
        flag = True
    
    if (first := word[0].lower()) in VOWELS:
        res = word + 'way'
    else:
        base = word[1:].capitalize() if flag else word[1:]
        res = base + first + 'ay'

    return res

def get_pila_sentence(sent: str)-> str:
    '''
    Шифруем поросячей латынью предложение
    '''

    words = sent.split(' ')
    res = []

    for word in words:
        res.append(get_pila_word(word))

    return ' '.join(res)

if __name__ == '__main__':
    res = get_pila_sentence('hello world')
    print(res)
