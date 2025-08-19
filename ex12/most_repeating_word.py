from collections import Counter
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def most_repeating_word_1(words_list: list[str]) -> str:
    '''
    Function without Counter
    '''
    res = [0, '']
    for word in words_list:
        letters = {}
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        wins = sorted(letters, key=lambda x: letters[x])
        win_letter = wins[-1]
        word_res = letters[win_letter]
        if word_res > res[0]:
            res = [word_res, word]
    return res[1]

def most_repeating_word_2(words_list: list[str]) -> str:
    '''
    Function with Counter
    '''
    res = ['', 0]
    for word in words_list:
        win = Counter(word).most_common(1)[0]
        if win[1] > res[1]:
            res[0], res[1] = word, win[1]
    return res[0]

def most_repeating_word_3(words_list: list[str]) -> str:
    '''
    Вариант решения из книги
    '''
    return max(words_list,
            key=most_repeating_letter_count)

def most_repeating_letter_count(word: str) -> int:
    '''
    Вспомогательная функция для most_repeating_word_3
    '''
    return Counter(word).most_common(1)[0][1]

def most_repeating_vowel_count(word: str) -> int:
    '''
    Вспомогательная функция для most_repeating_word_3
    Находит наибольшее количество повторений гласного
    звука в слове
    '''
    return max(Counter(word).most_common(),
            key=lambda x: x[0] in VOWELS)[1]


if __name__ == '__main__':
    check = most_repeating_vowel_count('aaabbbccceeee')
    print(check)
