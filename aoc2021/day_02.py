import os

import numpy as np


def task_1(data):
    current_pos = np.array([0, 0])  # horizontal, depth
    direction_map = {
        "forward": np.array([1, 0]),
        "up": np.array([0, -1]),
        "down": np.array([0, 1]),
    }
    for direction, value in data:
        current_pos += direction_map[direction] * value
    return current_pos[0] * current_pos[1]


def task_2(data):
    current_pos = np.array([0, 0])  # horizontal, depth
    direction_vector = np.array([1, 0])
    for direction, value in data:
        if direction == "forward":
            current_pos += direction_vector * value
        elif direction == "up":
            direction_vector[1] -= value
        elif direction == "down":
            direction_vector[1] += value
    return current_pos[0] * current_pos[1]


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_02.txt'):
        direction, value = line.replace('\n', '').split(' ')
        data.append((direction, int(value)))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
