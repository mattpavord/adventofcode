from string import digits


# have the digit, but also keep the first and last char incase they're needed in another
NUMBER_MAPPING = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def get_calibration_value(line: str) -> int:
    first, last = None, None
    for char in line:
        if char in digits:
            if first is None:
                first = int(char)
            last = int(char)
    return first * 10 + last


def task_1(data):
    return sum(get_calibration_value(line) for line in data)


def task_2(data):
    total = 0
    for line in data:
        # loop through string in groups of five to replace strings as digits
        line_copy = line
        for pos in range(len(line_copy) - 4):
            for key, value in NUMBER_MAPPING.items():
                if key in line_copy[pos: pos+5]:
                    line = line.replace(key, str(value))
        total += get_calibration_value(line)
    return total


def main():
    with open('data/day_01.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
