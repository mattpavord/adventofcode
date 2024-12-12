def check_update_correct(update: list[int], rules: list[list[int]]) -> bool:
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def task_1(rules, updates):
    total = 0
    for update in updates:
        if check_update_correct(update, rules):  # update is valid, get middle number
            total += update[len(update) // 2]
    return total


def task_2(rules, updates):
    total = 0
    bad_updates = []
    for update in updates:
        if not check_update_correct(update, rules):
            bad_updates.append(update)
    for update in bad_updates:
        while not check_update_correct(update, rules):
            for x, y in rules:
                if x in update and y in update:
                    x_index = update.index(x)
                    y_index = update.index(y)
                    if x_index > y_index:  # Swap x and y
                        update[x_index] = y
                        update[y_index] = x
        total += update[len(update) // 2]
    return total


def main():
    with open('data/day_05.txt', 'rt') as reader:
        data = reader.read().split("\n")
    rules = []
    updates = []
    for line in data:
        if "|" in line:
            rules.append([int(x) for x in line.split("|")])
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])
    print(task_1(rules, updates))
    print(task_2(rules, updates))


if __name__ == "__main__":
    main()
