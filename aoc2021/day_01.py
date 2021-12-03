import os


def task_1(data):
    n_larger = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            n_larger += 1
    return n_larger


def task_2(data):
    n_larger = 0
    for i in range(len(data) - 2):
        if sum(data[i+1:i+4]) > sum(data[i:i+3]):
            n_larger += 1
    return n_larger


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_01.txt'):
        data.append(int(line))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
