from typing import List, Union
import numpy as np


def initialise_grid(data: List[str], add_floor: bool = False) -> Union[np.array, int]:
    """
    Initialise grid on a numpy 2d int array, 0 represents free space, 1 for rock
    Returns the np.array and an integer representing the mapped x-coord of the falling sand
    """
    paths = []
    all_coords = []
    for line in data:
        coords = [
            (int(c.split(",")[0]), int(c.split(",")[1])) for c in line.split(" -> ")
        ]
        paths.append(coords)
        all_coords.extend(coords)

    extra_y = 2 if add_floor else 0
    max_y = max(c[1] for c in all_coords) + extra_y + 1

    if not add_floor:
        min_x = min(c[0] for c in all_coords) - 1  # add buffer either side
        max_x = max(c[0] for c in all_coords) + 1
    else:
        min_x = 500 - max_y - 2
        max_x = 500 + max_y + 2

    grid = np.zeros((max_y, max_x - min_x), dtype=int)
    for path in paths:
        for i in range(len(path) - 1):
            (x1, y1), (x2, y2) = path[i: i + 2]
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y, x - min_x] = 1

    if add_floor:
        for x in range(max_x - min_x):
            grid[max_y-1, x] = 1

    return grid, 500 - min_x


def simulate_sand_fall(grid, x_sand):
    max_y, max_x = grid.shape
    sand_falling = True
    while sand_falling:
        x = x_sand
        for y in range(max_y):
            for dx in (0, -1, 1):
                if x + dx < 0 or x + dx >= max_x:
                    continue
                if grid[y, x+dx] == 0:
                    x += dx
                    break
            else:  # sand has come to a stop
                grid[y-1, x] = 2
                break
        else:
            sand_falling = False
        if grid[0, x_sand] == 2:
            sand_falling = False
    return len(np.where(grid == 2)[0])


def task_1(data):
    grid, x_sand = initialise_grid(data)
    return simulate_sand_fall(grid, x_sand)


def task_2(data):
    grid, x_sand = initialise_grid(data, add_floor=True)
    return simulate_sand_fall(grid, x_sand)


def main():
    with open("data/day_14.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
