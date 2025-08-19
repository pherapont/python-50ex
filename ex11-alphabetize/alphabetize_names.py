from operator import itemgetter
from typing import List, Dict
from pprint import pprint
from names_data import PEOPLE


def alphabetize_names_0(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    '''
    input: list[dict['first:, last:, email:]]
    output: same list sorted by last
    variant 0 with adding transforming to list for sorting
    '''
    tmp_list = [(item['last'], item['first'], item['email']) for item in data]
    tmp_list.sort(key=lambda x: (x[0], x[1]))

    res = [dict(zip(('last', 'first', 'email'), item)) for item in tmp_list]
    return res


def alphabetize_names_1(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    '''
    input: list[dict['first:, last:, email:]]
    output: same list sorted by last and first
    variant 1 without transforming to list
    '''
    res = sorted(data, key=lambda x: (x['last'], x['first']))
    return res


def alphabetize_names_2(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    '''
    input: list[dict['first:, last:, email:]]
    output: same list sorted by last and first
    variant 2 with itemgettrs
    '''
    res = sorted(data, key=itemgetter('last', 'first'))
    return res


if __name__ == '__main__':
    res = alphabetize_names_2(PEOPLE)
    pprint(res)
