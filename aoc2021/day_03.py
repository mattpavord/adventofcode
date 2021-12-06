from typing import List
import os

import numpy as np


def binary_to_int(binary: List[int]) -> int:
    output = 0
    for i in range(len(binary)):
        output += int(binary[-1*(i+1)]) * 2**i
    return output


def get_most_common_bits(data, reverse=False):
    total = np.zeros(len(list(data)[0]), dtype=float)
    for line in data:
        total += np.array([int(x) for x in line])
    total /= len(data)
    if reverse:
        return [0 if x >= 0.5 else 1 for x in total]
    else:
        return [1 if x >= 0.5 else 0 for x in total]


def filter_down_data_set_on_most_common_bit(data, reverse=False):
    data_set = set(data)
    for i in range(len(data[0])):
        most_common_bit = get_most_common_bits(data_set, reverse=reverse)[i]
        to_remove = set()
        for binary in data_set:
            if int(binary[i]) != most_common_bit:
                to_remove.add(binary)
        data_set -= to_remove
        if len(data_set) < 2:
            break
    assert len(data_set) == 1
    return list(data_set)[0]


def task_1(data):
    binary_gamma = get_most_common_bits(data)
    binary_epsilon = get_most_common_bits(data, reverse=True)
    return binary_to_int(binary_gamma) * binary_to_int(binary_epsilon)


def task_2(data):
    binary_oxygen = filter_down_data_set_on_most_common_bit(data)
    binary_co2 = filter_down_data_set_on_most_common_bit(data, reverse=True)
    return binary_to_int(binary_oxygen) * binary_to_int(binary_co2)


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_03.txt'):
        line = line.replace('\n', '')
        data.append(line)
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
