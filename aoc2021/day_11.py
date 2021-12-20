import os

import numpy as np


def flash(octopus_map, coords):
    x, y = coords
    n_flashes = 1
    octopus_map[x, y] = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        try:
            if x+dx < 0 or y + dy < 0:
                raise IndexError
            if octopus_map[x+dx, y+dy] > 0:
                octopus_map[x+dx, y+dy] += 1
                if octopus_map[x+dx, y+dy] >= 10:
                    n_flashes += flash(octopus_map, (x+dx, y+dy))
        except IndexError:
            pass
    return n_flashes


def task_1(data):
    octopus_map = data.copy()
    n_flashes = 0
    max_x, max_y = octopus_map.shape
    for _ in range(100):
        octopus_map += 1
        for x in range(max_x):
            for y in range(max_y):
                if octopus_map[x, y] == 10:
                    n_flashes += flash(octopus_map, (x, y))
    return n_flashes


def task_2(data):
    octopus_map = data.copy()
    n_steps = 0
    max_x, max_y = octopus_map.shape
    while sum(octopus_map.ravel()):
        octopus_map += 1
        for x in range(max_x):
            for y in range(max_y):
                if octopus_map[x, y] == 10:
                    flash(octopus_map, (x, y))
        n_steps += 1
    return n_steps


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_11.txt'):
        data.append([int(x) for x in line.replace('\n', '')])
    data = np.array(data)
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
