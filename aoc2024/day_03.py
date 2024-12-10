import re


def task_1(data):
    total = 0
    for line in data:
        muls = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in muls:
            a, b = mul[4:].replace(")", "").split(",")
            total += int(a) * int(b)
    return total


def task_2(data):
    total = 0
    enabled_mul = True
    for line in data:
        matches = re.findall(r"(mul\(\d+,\d+\))|(don't)|(do)", line)
        # matches - [('mul(2,4)', '', ''), ('', "don't", ''), ('', '', 'do')]
        for match in matches:
            if match[0]:
                if enabled_mul:
                    a, b = match[0][4:].replace(")", "").split(",")
                    total += int(a) * int(b)
            if match[1]:
                enabled_mul = False
            if match[2]:
                enabled_mul = True
    return total



def main():
    with open('data/day_03.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
