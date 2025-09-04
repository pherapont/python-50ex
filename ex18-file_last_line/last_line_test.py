'''
Идея по тестированию функции get_final_line: создаем тестовый файл,
записываем в него несколько строк, потом применяем к нему get_final_line, 
и в результате должны получить последнюю строку.
'''

strings = [
        'My little friend.',
        'I want to send your',
        'it little present.',
        ]

test_file = 'test_lines.txt'

with open(test_file, 'w') as tf:
    for line in strings:
        tf.write(line)
        tf.write('\n')

