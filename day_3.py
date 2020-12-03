import os
from typing import List


def find_trees(slope_data: List[str], right_velocity: int, down_velocity: int):
    slope_width = len(slope_data[0])
    x = 0
    n_trees_found = 0
    for i in range(len(slope_data)):
        y = i * down_velocity
        if y > len(slope_data):
            return n_trees_found
        line = slope_data[y]
        if line[x] == '#':
            n_trees_found += 1
        x += right_velocity
        if x >= slope_width:
            x -= slope_width
    return n_trees_found


def task_1(slope_data: List[str]):
    return find_trees(slope_data, 3, 1)


def task_2(slope_data: List[str]):
    answer = 1
    slopes_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for x_vel, y_vel in slopes_to_check:
        answer *= find_trees(slope_data, x_vel, y_vel)
    return answer


def main():
    slope_data = []
    for line in open(os.getcwd() + '/data/day_3.txt'):
        slope_data.append(line.replace('\n', ''))
    print(task_1(slope_data))
    print(task_2(slope_data))


if __name__ == '__main__':
    main()
