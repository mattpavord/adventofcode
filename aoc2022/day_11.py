class Monkey:
    def __init__(self, raw_data):
        lines = raw_data.split("\n")
        self.items = [int(item) for item in lines[1][18:].split(", ")]
        self.operation = lines[2][19:]
        self.test_divisible_by = int(lines[3][20:])
        self.monkey_if_true = int(lines[4][29:])
        self.monkey_if_false = int(lines[5][30:])
        self.counted_items = 0

    def apply_operation(self, number):
        if "*" in self.operation:
            x1, x2 = self.operation.split(" * ")
            func = lambda a, b: a * b
        else:
            x1, x2 = self.operation.split(" + ")
            func = lambda a, b: a + b
        x1 = number if x1 == "old" else int(x1)
        x2 = number if x2 == "old" else int(x2)
        return func(x1, x2)


def iterate_monkeys(data, n_rounds, part_1=True):
    monkeys = [Monkey(monkey_data) for monkey_data in data]
    lowest_common_multiple = 1
    for monkey in monkeys:
        lowest_common_multiple *= monkey.test_divisible_by

    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.counted_items += len(monkey.items)
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                item = monkey.apply_operation(item)
                if part_1:
                    item = item // 3
                else:
                    # only care if it's a remainder of the test numbers, so can reduce it by
                    # their lowest common multiple
                    item = item % lowest_common_multiple
                if item % monkey.test_divisible_by == 0:
                    next_monkey_id = monkey.monkey_if_true
                else:
                    next_monkey_id = monkey.monkey_if_false
                monkeys[next_monkey_id].items.append(item)
    busy_monkeys = sorted(monkeys, key=lambda x: x.counted_items, reverse=True)
    return busy_monkeys[0].counted_items * busy_monkeys[1].counted_items


def task_1(data):
    return iterate_monkeys(data, 20)


def task_2(data):
    return iterate_monkeys(data, 10000, part_1=False)


def main():
    with open('data/day_11.txt', 'rt') as reader:
        data = reader.read().split("\n\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
