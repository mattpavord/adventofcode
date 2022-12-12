import string

import numpy as np


def get_coords(data, char):
    location = np.where(data == char)
    return location[1][0], location[0][0]  # x, y


def get_height(height_char):
    """ Given height char, return an integer """
    special_coord_map = {"S": "a", "E": "z"}
    if height_char in special_coord_map:
        height_char = special_coord_map[height_char]
    return string.ascii_lowercase.index(height_char)


def track_path(start_coords, data):
    destination_reached = False
    end_coords = get_coords(data, "E")
    distance_maps = {start_coords: 0}  # coords to distance from start
    visited_coords = set()
    x, y = start_coords

    while not destination_reached:
        current_height = get_height(data[(y, x)])
        visited_coords.add((x, y))
        distance = distance_maps[(x, y)]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            try:
                if y + dy < 0 or x + dx < 0:
                    raise IndexError
                new_height = get_height(data[y+dy, x+dx])
            except IndexError:
                continue
            if new_height - current_height > 1:
                continue
            else:
                new_distance = distance + 1
                coords = (x+dx, y+dy)
                if coords in visited_coords:
                    continue
                if coords not in distance_maps or new_distance < distance_maps[coords]:
                    distance_maps[coords] = new_distance

        if (x, y) == end_coords:
            destination_reached = True

        else:
            possible_next_coords = set(distance_maps.keys()) - visited_coords
            x, y = sorted(possible_next_coords, key=lambda c: distance_maps[c])[0]

    return distance_maps[end_coords]


def task_1(data):
    start_coords = get_coords(data, "S")
    return track_path(start_coords, data)


def task_2(data):
    return


def main():
    with open('data/day_12.txt', 'rt') as reader:
        raw_data = reader.read().split("\n")
        data = np.zeros((len(raw_data), len(raw_data[0])), dtype=str)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                data[i, j] = raw_data[i][j]
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
