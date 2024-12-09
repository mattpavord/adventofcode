from string import digits


def is_symbol(char: str) -> bool:
    if char in digits:
        return False
    return char != "."


def task_1(data):
    total = 0
    symbol_adjacent = False
    number_str = ""
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in digits:
                number_str += data[y][x]
                if not symbol_adjacent:
                    # Adjacents
                    if y > 0 and is_symbol(data[y - 1][x]):
                        symbol_adjacent = True
                    if y < len(data) - 1 and is_symbol(data[y + 1][x]):
                        symbol_adjacent = True
                    if x > 0 and is_symbol(data[y][x - 1]):
                        symbol_adjacent = True
                    if x < len(data[y]) - 1 and is_symbol(data[y][x + 1]):
                        symbol_adjacent = True
                    # Diagonals
                    if y > 0 and x > 0 and is_symbol(data[y - 1][x - 1]):
                        symbol_adjacent = True
                    if y > 0 and x < len(data[y]) - 1 and is_symbol(data[y - 1][x + 1]):
                        symbol_adjacent = True
                    if y < len(data) - 1 and x > 0 and is_symbol(data[y + 1][x - 1]):
                        symbol_adjacent = True
                    if y < len(data) - 1 and x < len(data[y]) - 1 and is_symbol(
                        data[y + 1][x + 1]
                    ):
                        symbol_adjacent = True
            elif number_str:
                number = int(number_str)
                print(number, symbol_adjacent)
                if symbol_adjacent:
                    total += number
                    symbol_adjacent = False
                number_str = ""
    return total



def task_2(data):
    return


def main():
    with open('data/day_03.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
