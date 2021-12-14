import os


def iterate_n_days(data, n_days):
    population = [0] * 9
    # population is a list of quantities - index being days until reproduction
    for x in data:
        population[x] += 1
    for _ in range(n_days):
        n_new = population.pop(0)
        population[6] += n_new
        population.append(n_new)
    return sum(population)


def task_1(data):
    return iterate_n_days(data, n_days=80)


def task_2(data):
    return iterate_n_days(data, n_days=256)


def main():
    for line in open(os.getcwd() + '/data/day_06.txt'):
        data = [int(x) for x in line.split(',')]
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
