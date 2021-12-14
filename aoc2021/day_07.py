import os

import numpy as np


def task_1(data):
    min_fuel = None
    for i in range(min(data), max(data)):
        fuel_spent = sum(abs(data - i))
        if min_fuel is None or fuel_spent < min_fuel:
            min_fuel = fuel_spent
    return min_fuel


def triangle_number(x):
    return sum(range(1, x+1))


def task_2(data):
    min_fuel = None
    for i in range(min(data), max(data)):
        fuel_spent_per_crab = [triangle_number(x) for x in abs(data - i)]
        fuel_spent = sum(fuel_spent_per_crab)
        if min_fuel is None or fuel_spent < min_fuel:
            min_fuel = fuel_spent
    return min_fuel


def main():
    for line in open(os.getcwd() + '/data/day_07.txt'):
        data = np.array([int(x) for x in line.split(',')])
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
