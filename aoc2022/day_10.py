def task_1(data):
    x = 1
    cycle = 1
    check_cycles = [20, 60, 100, 140, 180, 220]
    total = 0
    for line in data:
        if line == "noop":
            cycle += 1
            value = 0
        else:
            cycle += 2
            value = int(line.split(" ")[1])
        if cycle > check_cycles[0]:
            total += x * check_cycles.pop(0)
        x += value
        if not check_cycles:
            return total


def task_2(data):
    cpu_pos = 0
    x = 1
    output = []
    current_row = ""
    for line in data:
        if line == "noop":
            n_cycles = 1
            value = 0
        else:
            n_cycles = 2
            value = int(line.split(" ")[1])

        for _ in range(n_cycles):
            pixel = "#" if x - 1 <= cpu_pos <= x + 1 else "."
            current_row += pixel
            cpu_pos += 1

            if len(current_row) % 40 == 0:
                cpu_pos -= 40
                output.append(current_row)
                current_row = ""
        x += value

    return "\n".join(output)


def main():
    with open('data/day_10.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
