def find_distinct(data, n):
    for i in range(n, len(data)):
        if len(set(char for char in data[i-n:i])) == n:
            return i


def task_1(data):
    return find_distinct(data, 4)


def task_2(data):
    return find_distinct(data, 14)


def main():
    with open('data/day_06.txt', 'rt') as reader:
        data = reader.read()
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
