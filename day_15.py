from typing import List


def find_nth_number(n: int, starting_numbers: List[int]) -> int:
    last_positions = {}
    new_number = 0
    for i in range(n):
        current_number = new_number
        if i < len(starting_numbers):
            last_positions[current_number] = i
            new_number = starting_numbers[i]
        elif current_number in last_positions:
            new_number = i - last_positions[current_number]
        else:
            last_positions[current_number] = i
            new_number = 0
        last_positions[current_number] = i
    return new_number


def task_1(starting_numbers: List[int]) -> int:
    return find_nth_number(2020, starting_numbers)


def task_2(starting_numbers: List[int]) -> int:
    return find_nth_number(30000000, starting_numbers)


def main():
    lines = []
    for line in open('data/day_15.txt'):
        lines.append(line.replace('\n', ''))
        break
    numbers = [int(x) for x in lines[0].split(',')]
    print(task_1(numbers))
    print(task_2(numbers))


if __name__ == '__main__':
    main()
