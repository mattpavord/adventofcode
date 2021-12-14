import os

import numpy as np


def construct_map(data):
    max_n = 0
    for (x1, y1), (x2, y2) in data:
        max_n = max([max_n, x1, x2, y1, y2])
    return np.zeros((max_n+1, max_n+1), dtype=int)


def task_1(data):
    g_map = construct_map(data)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y2 > y1:
                g_map[x1, y1:y2+1] += 1
            else:
                g_map[x1, y2:y1+1] += 1
        if y1 == y2:
            if x2 > x1:
                g_map[x1:x2+1, y1] += 1
            else:
                g_map[x2:x1+1, y1] += 1
    return sum(np.bincount(g_map.ravel())[2:])


def task_2(data):
    g_map = construct_map(data)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y2 > y1:
                g_map[x1, y1:y2+1] += 1
            else:
                g_map[x1, y2:y1+1] += 1
        elif y1 == y2:
            if x2 > x1:
                g_map[x1:x2+1, y1] += 1
            else:
                g_map[x2:x1+1, y1] += 1
        else:
            if y2 > y1 and x2 > x1:
                for i in range(y2 - y1 + 1):
                    g_map[x1+i, y1+i] += 1
            if y2 > y1 and x1 > x2:
                for i in range(y2 - y1 + 1):
                    g_map[x1-i, y1+i] += 1
            if y1 > y2 and x2 > x1:
                for i in range(y1 - y2 + 1):
                    g_map[x1+i, y1-i] += 1
            if y1 > y2 and x1 > x2:
                for i in range(y1 - y2 + 1):
                    g_map[x1-i, y1-i] += 1
    return sum(np.bincount(g_map.ravel())[2:])


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_05.txt'):
        c1, c2 = line.replace('\n', '').split(' -> ')
        data.append([[int(x) for x in c.split(',')] for c in [c1, c2]])
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
