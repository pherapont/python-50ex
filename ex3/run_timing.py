def run_timing():
    run_count = 0
    run_com_time = 0

    for i in range(5):
        print(i)
        
    while (ans := input("Введите время пробега 10 км: ")):
        if ans:
            try:
                run_time = int(ans)
            except ValueError:
                print("Время - это число!")
                continue
            run_count += 1
            run_com_time += run_time

    res = run_com_time / run_count
    print(f"Средний показатель {res}, более {run_count} пробежек.")

if __name__ == '__main__':
    run_timing()
