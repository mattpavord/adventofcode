import os


def task_1(data):
    return max(sum(group) for group in data)


def task_2(data):
    total_calories = [sum(group) for group in data]
    return sum(sorted(total_calories)[-3:])


def main():
    data = []
    data_group = []  # separate into lists, separated by the linebreak
    for line in open(os.getcwd() + '/data/day_01.txt'):
        line = line.replace("\n", "")
        if line:
            data_group.append(int(line))
        else:
            data.append(data_group)
            data_group = []
    data.append(data_group)
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
