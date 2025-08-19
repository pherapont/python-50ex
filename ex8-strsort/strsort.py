'''
Module for implementation string sorting
'''

def strsort(istr: str) -> str:
    '''
    Function get string ang output sorting increase way 
    string
    '''
    arr_str = list(istr)
    print (arr_str)
    arr_str.sort()
    print(arr_str)
    return ''.join(arr_str)

if __name__ == '__main__':
    res = strsort('bca')
    print(res)
