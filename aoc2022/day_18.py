import numpy as np

DIRECTIONS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def init_3d_array(data):
    x_max = max(d[0] for d in data) + 2
    y_max = max(d[1] for d in data) + 2
    z_max = max(d[2] for d in data) + 2
    array = np.zeros((x_max, y_max, z_max), dtype=int)
    for x, y, z in data:
        array[x, y, z] = 1
    return array


def label_external_coords(array):
    """ Make external 0s into 2s """
    x_max, y_max, z_max = array.shape
    coords_to_fill = [(0, 0, 0)]
    while coords_to_fill:
        x, y, z = coords_to_fill.pop(0)
        if array[x, y, z] == 2:
            continue
        array[x, y, z] = 2
        for dx, dy, dz in DIRECTIONS:
            if 0 <= x + dx < x_max and 0 <= y + dy < y_max and 0 <= z + dz < z_max:
                if array[x + dx, y + dy, z + dz] == 0:
                    coords_to_fill.append((x+dx, y+dy, z+dz))


def task_1(data):
    array = init_3d_array(data)
    total_facing_sides = 0
    for x, y, z in data:
        for dx, dy, dz in DIRECTIONS:
            if array[x + dx, y + dy, z + dz] == 0:
                total_facing_sides += 1
    return total_facing_sides


def task_2(data):
    array = init_3d_array(data)
    label_external_coords(array)
    total_facing_sides = 0
    for x, y, z in data:
        for dx, dy, dz in DIRECTIONS:
            if array[x + dx, y + dy, z + dz] == 2:
                total_facing_sides += 1
    return total_facing_sides


def main():
    with open("data/day_18.txt", "rt") as reader:
        data = reader.read().split("\n")
        data = [[int(i) for i in row.split(",")] for row in data]
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
