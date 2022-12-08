import numpy as np


def task_1(data):
    max_y, max_x = data.shape
    n_visible_coords = 0
    for x in range(max_x):
        for y in range(max_y):
            # check right
            for xx in range(x+1, max_x):
                if data[y, xx] >= data[y, x]:
                    break
            else:
                n_visible_coords += 1
                continue

            # check left
            for xx in range(0, x):
                if data[y, xx] >= data[y, x]:
                    break
            else:
                n_visible_coords += 1
                continue

            # check down (increasing y goes down)
            for yy in range(y+1, max_y):
                if data[yy, x] >= data[y, x]:
                    break
            else:
                n_visible_coords += 1
                continue

            # check up
            for yy in range(0, y):
                if data[yy, x] >= data[y, x]:
                    break
            else:
                n_visible_coords += 1
                continue

    return n_visible_coords


def task_2(data):
    max_y, max_x = data.shape
    best_scenic_score = 0

    for x in range(max_x):
        for y in range(max_y):
            east = west = north = south = 0
            # check right
            for xx in range(x+1, max_x):
                east += 1
                if data[y, xx] >= data[y, x]:
                    break

            # check left
            for xx in reversed(range(0, x)):
                west += 1
                if data[y, xx] >= data[y, x]:
                    break

            # check down (increasing y goes down)
            for yy in range(y+1, max_y):
                south += 1
                if data[yy, x] >= data[y, x]:
                    break

            # check up
            for yy in reversed(range(0, y)):
                north += 1
                if data[yy, x] >= data[y, x]:
                    break

            scenic_score = north * west * south * east
            best_scenic_score = max(scenic_score, best_scenic_score)

    return best_scenic_score


def main():
    with open('data/day_08.txt', 'rt') as reader:
        data = np.array([[int(x) for x in row] for row in reader.read().split("\n")])
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
