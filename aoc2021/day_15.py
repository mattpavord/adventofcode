import os
import time

import numpy as np


def track_path(data):
    t0 = time.time()
    time_check = 60
    max_y, max_x = data.shape
    distance_maps = {(0, 0): 0}  # coords to distance from origin
    destination_reached = False
    x = y = 0
    visited_coords = set()
    while not destination_reached:
        visited_coords.add((x, y))
        tentative_distance = distance_maps[(x, y)]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            try:
                value = data[y+dy, x+dx]
                if x+dx < 0 or y+dy < 0:
                    raise IndexError
            except IndexError:
                pass
            else:
                new_distance = tentative_distance + value
                coords = (x+dx, y+dy)
                if coords in visited_coords:
                    continue
                if coords not in distance_maps or new_distance < distance_maps[coords]:
                    distance_maps[coords] = new_distance

        if x == max_x - 1 and y == max_y - 1:
            destination_reached = True

        if not destination_reached:
            possible_next_coords = set(distance_maps.keys()) - visited_coords
            x, y = sorted(possible_next_coords, key=lambda c: distance_maps[c])[0]

        time_passed = time.time() - t0
        if time_passed > time_check:
            print(x, y)
            time_check += 60

    return distance_maps[(max_x-1, max_y-1)]


def task_1(data):
    return track_path(data)


def task_2(data):
    max_x, max_y = data.shape
    expanded_data = np.zeros((max_x*5, max_y*5), dtype=int)
    for i in range(5):
        for j in range(5):
            expanded_data[i*max_y: (i+1)*max_y, j*max_x: (j+1)*max_x] = data + i + j
    expanded_data = ((expanded_data - 1) % 9) + 1
    return track_path(expanded_data)


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_15.txt'):
        data.append([int(x) for x in line.replace('\n', '')])
    data = np.array(data)
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
