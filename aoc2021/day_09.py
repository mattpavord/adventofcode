import os

import numpy as np


def get_adjacent_coords(coords, max_coords):
    x, y = coords
    max_x, max_y = max_coords
    adjacents = []
    if x:
        adjacents.append((x - 1, y))
    if x != max_x - 1:
        adjacents.append((x + 1, y))
    if y:
        adjacents.append((x, y - 1))
    if y != max_y - 1:
        adjacents.append((x, y + 1))
    return adjacents


def get_low_points(data):
    max_x, max_y = data.shape
    low_points = []
    for x in range(max_x):
        for y in range(max_y):
            adjacent_coords = get_adjacent_coords((x, y), data.shape)
            adjacent_values = [data[x, y] for x, y in adjacent_coords]
            if data[x, y] < min(adjacent_values):
                low_points.append((x, y))
    return low_points


def task_1(data):
    total = 0
    for x, y in get_low_points(data):
        total += data[x, y] + 1
    return total


def task_2(data):
    low_points = get_low_points(data)
    basin_sizes = []
    for low_x, low_y in low_points:
        current_iteration = {(low_x, low_y)}
        previous_iterations = set()
        while current_iteration:
            next_iterations = set()
            previous_iterations = set.union(previous_iterations, current_iteration)
            for coord in current_iteration:
                next_iterations = set.union(next_iterations, set([
                    (x, y)
                    for x, y in get_adjacent_coords(coord, data.shape)
                    if data[x, y] < 9 and (x, y) not in previous_iterations
                ]))
            current_iteration = next_iterations
        basin_sizes.append(len(previous_iterations))

    product = 1
    for x in sorted(basin_sizes, reverse=True)[:3]:
        product *= x
    return product


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_09.txt'):
        data.append([int(x) for x in line.replace('\n', '')])
    data = np.array(data)
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
