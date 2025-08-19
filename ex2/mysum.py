def mysum (*args):
    res = 0

    for arg in args:
        res += arg

    return res

if __name__ == '__main__':
    print(mysum(1, 2, 3, 4, 5, 6))
