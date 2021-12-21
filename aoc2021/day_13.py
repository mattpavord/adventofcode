import os

import numpy as np
import matplotlib.pyplot as plt


def fold_dots(dots, folds):
    next_dots = set()
    for fold in folds:
        next_dots = set()
        direction = fold[0]
        value = int(fold[2:])
        for x, y in dots:
            if direction == 'x':
                x = 2 * value - x if x > value else x
            else:
                y = 2 * value - y if y > value else y
            next_dots.add((x, y))
        dots = next_dots.copy()
    return next_dots


def task_1(dots, folds):
    folds = [folds[0]]
    dots = fold_dots(dots, folds)
    return len(dots)


def task_2(dots, folds):
    dots = fold_dots(dots, folds)
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    pattern = np.full((max_x+1, max_y+1), fill_value='.')
    for x, y in dots:
        pattern[x, y] = '#'
    return pattern


def main():
    dots = []
    folds = []
    for line in open(os.getcwd() + '/data/day_13.txt'):
        line = line.replace('\n', '')
        if not line:
            continue
        elif line.startswith("fold along"):
            folds.append(line[11:])
        else:
            dots.append(tuple([int(x) for x in line.split(',')]))
    print(task_1(dots, folds))
    print(task_2(dots, folds))


if __name__ == '__main__':
    main()
