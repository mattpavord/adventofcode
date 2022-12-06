import string


def get_priority(char):
    if char in string.ascii_lowercase:
        return string.ascii_lowercase.index(char) + 1
    return string.ascii_uppercase.index(char) + 27


def task_1(data):
    total = 0
    for bag in data:
        compartment_1 = bag[:len(bag)//2]
        compartment_2 = bag[len(bag)//2:]
        shared = set(compartment_1).intersection(set(compartment_2))
        total += sum(get_priority(char) for char in shared)
    return total


def task_2(data):
    total = 0
    for i in range(len(data) // 3):
        group = data[3*i:3*i+3]
        shared = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total += get_priority(list(shared)[0])
    return total


def main():
    data = []
    for line in open("data/day_03.txt"):
        data.append(line.replace("\n", ""))

    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
