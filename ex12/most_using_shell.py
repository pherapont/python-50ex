'''
1. Читаем файл построчно (формат строки usr:str:str:str:...:shell)
    в dict(shell: [usr1, usr2,...,]) def read_shell_file(sf_path)
'''
from collections import Counter

SHELLS_PATH = '/etc/passwd'

def read_shell_file(sf_path):
    '''
    Читаем файл построчно (формат строки usr:str:str:str:...:shell)
    в dict(shell: [usr1, usr2,...,]) 
    '''
    with open(sf_path, 'rt') as sf_file:
        res = {}
        for line in sf_file:
            data = line.strip().split(':')
            name, row_shell = data[0], data[-1]
            shell = row_shell.split('/')[-1]
            if shell in res:
                res[shell].append(name)
            else:
                res[shell] = [name]
    return res

def most_using_shell():
    data = read_shell_file(SHELLS_PATH)
    scores = {key: len(value) for key, value in data.items()}
    res = Counter(scores).most_common()
    print(res)
    return [line[0] for line in res]
    
if __name__ == '__main__':
    shells = most_using_shell()
    print(shells)
