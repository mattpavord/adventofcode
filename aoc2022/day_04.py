import os


def task_1(data):
    total = 0
    for p1_min, p1_max, p2_min, p2_max in data:
        if p1_max >= p2_max and p1_min <= p2_min:
            total += 1
        elif p2_max >= p1_max and p2_min <= p1_min:
            total += 1
    return total


def task_2(data):
    total = 0
    for p1_min, p1_max, p2_min, p2_max in data:
        if p2_max >= p1_max >= p2_min or p2_max >= p1_min >= p2_min:
            total += 1
        elif p1_max >= p2_max >= p1_min or p1_max >= p2_min >= p1_min:
            total += 1
    return total


def main():
    data = []
    for line in open(os.getcwd() + "/data/day_04.txt"):
        line = line.replace("\n", "")
        data.append([int(n) for x in line.split(",") for n in x.split("-")])

    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
