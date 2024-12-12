def task_1(data):
    count = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c != "X":
                continue
            if i >= 3:
                if data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
                    count += 1
            if i <= len(data) - 4:
                if data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
                    count += 1
            if j >= 3:
                if data[i][j - 1] == "M" and data[i][j - 2] == "A" and data[i][j - 3] == "S":
                    count += 1
            if j <= len(line) - 4:
                if data[i][j + 1] == "M" and data[i][j + 2] == "A" and data[i][j + 3] == "S":
                    count += 1
            if i >= 3 and j >= 3:
                if data[i - 1][j - 1] == "M" and data[i - 2][j - 2] == "A" and data[i - 3][j - 3] == "S":
                    count += 1
            if i <= len(data) - 4 and j <= len(line) - 4:
                if data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
                    count += 1
            if i >= 3 and j <= len(line) - 4:
                if data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
                    count += 1
            if i <= len(data) - 4 and j >= 3:
                if data[i + 1][j - 1] == "M" and data[i + 2][j - 2] == "A" and data[i + 3][j - 3] == "S":
                    count += 1
    return count


def task_2(data):
    count = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if i == 0 or j == 0 or i == len(data) - 1 or j == len(line) - 1:
                continue
            if c != "A":
                continue
            line_1 = "".join([data[i - 1][j - 1], "A", data[i + 1][j + 1]])
            line_2 = "".join([data[i - 1][j + 1], "A", data[i + 1][j - 1]])
            if line_1 in ["MAS", "SAM"] and line_2 in ["MAS", "SAM"]:
                count += 1
    return count


def main():
    with open('data/day_04.txt', 'rt') as reader:
        str_data = reader.read().split("\n")
    data = [[c for c in line] for line in str_data]
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
