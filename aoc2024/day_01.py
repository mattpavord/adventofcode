def task_1(data):
    first_list = sorted([x[0] for x in data])
    second_list = sorted([x[1] for x in data])
    return sum(abs(x - y) for x, y in zip(first_list, second_list))


def task_2(data):
    first_list = sorted([x[0] for x in data])
    second_list = sorted([x[1] for x in data])
    similarity_score = 0
    for x in first_list:
        similarity_score += x * second_list.count(x)
    return similarity_score


def main():
    with open('data/day_01.txt', 'rt') as reader:
        str_data = reader.read().split("\n")
    data = [
        (int(line.split("   ")[0]), int(line.split("   ")[1]))
        for line in str_data
    ]
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
