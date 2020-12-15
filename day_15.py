from typing import List
import numpy as np


def task_1(starting_numbers: List[int]) -> int:
    data = -1 * np.ones(2020, dtype=int)  # use -1 as empty value since it can't be used
    data[:len(starting_numbers)] = starting_numbers
    for i in range(len(data)):
        if data[i] == -1:
            prev_number = data[i-1]
            locations = np.where(data == prev_number)[0]
            data[i] = 0 if len(locations) == 1 else locations[-1] - locations[-2]
    return data[-1]


def main():
    lines = []
    for line in open('data/day_15.txt'):
        lines.append(line.replace('\n', ''))
        break
    numbers = [int(x) for x in lines[0].split(',')]
    print(task_1(numbers))
    # print(task_2(numbers))


if __name__ == '__main__':
    main()
