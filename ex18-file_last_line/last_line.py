def get_final_line(file_name):
    with open(file_name, 'r') as tf:
        prev = ''
        for line in tf:
            print(prev, ' => ', line)
            if not line:
                break
            prev = line
        return prev


if __name__ == '__main__':
    res = get_final_line('test_lines.txt')
    print(res)
