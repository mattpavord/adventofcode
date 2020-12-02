import os


def task_1(numbers: set):
    for number in numbers:
        number_required = 2020 - number
        if number_required in numbers:
            print(number * number_required)
            break
    else:
        print("Not found")


def task_2(numbers: set):
    found = False
    for number_1 in numbers:
        for number_2 in numbers:
            if number_1 == number_2:
                continue
            number_required = 2020 - number_1 - number_2
            if number_required in numbers:
                print(number_1 * number_2 * number_required)
                found = True
                break
        if found:
            break
    else:
        print("Not found")


def main():
    data = set()
    for line in open(os.getcwd() + '/data/day_1.txt'):
        data.add(int(line))
    task_1(data)
    task_2(data)


if __name__ == '__main__':
    main()
