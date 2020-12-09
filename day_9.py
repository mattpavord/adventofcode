from typing import List


def task_1(numbers: List[int]) -> int:
    for i in range(25, len(numbers)):
        target = numbers[i]
        previous_numbers = set(numbers[i-25: i])  # 2 of these should add up to target
        for number in previous_numbers:
            number_required = target - number
            if number_required != number and number_required in previous_numbers:
                break  # found pair
        else:
            return target
    raise Exception("Could not find incorrect number")


def task_2(numbers: List[int], invalid_number: int) -> int:
    for i in range(len(numbers)):
        sum_of_numbers = numbers[i]
        j = i
        while sum_of_numbers < invalid_number:
            j += 1
            sum_of_numbers += numbers[j]
        if sum_of_numbers == invalid_number:
            addition_list = numbers[i: j]
            addition_list.sort()
            return addition_list[0] + addition_list[-1]
    raise Exception("Could not find set of numbers that add to the invalid_number")


def main():
    numbers = []
    for line in open('data/day_9.txt'):
        numbers.append(int(line.replace('\n', '')))
    invalid_number = task_1(numbers)
    print(invalid_number)
    print(task_2(numbers, invalid_number))


if __name__ == '__main__':
    main()
