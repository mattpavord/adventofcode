import numpy as np


def init_3d_array(data):
    x_max = max(d[0] for d in data) + 2
    y_max = max(d[1] for d in data) + 2
    z_max = max(d[2] for d in data) + 2
    array = np.zeros((x_max, y_max, z_max), dtype=int)
    for x, y, z in data:
        array[x, y, z] = 1
    return array


def task_1(data):
    array = init_3d_array(data)
    total_facing_sides = 0
    for x, y, z in data:
        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if array[x+dx, y+dy, z+dz] == 0:
                total_facing_sides += 1
    return total_facing_sides


def task_2(data):
    array = init_3d_array(data)
    total_facing_sides = 0
    for x, y, z in data:
        facing_sides = 0
        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if array[x+dx, y+dy, z+dz] == 0:
                facing_sides += 1
        if facing_sides != 6:
            total_facing_sides += facing_sides
    return total_facing_sides


def main():
    with open('data/day_18.txt', 'rt') as reader:
        data = reader.read().split("\n")
        data = [[int(i) for i in row.split(",")] for row in data]
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
