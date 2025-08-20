from collections import namedtuple
from operator import itemgetter
from pprint import pprint
from format_records_test_data import PEOPLE

def format_records(data):
    sorted_list = sorted(data, key=itemgetter(1))

    Person = namedtuple('Person', 'name, surname, arrive_time')
    persons = [Person(*line) for line in sorted_list]
    
    format_list = [f"{person.surname:10}->{person.name:10}->{person.arrive_time:5.2f}"
    for person in persons]

    return '\n'.join(format_list)

if __name__ == '__main__':
    pprint(format_records(PEOPLE))