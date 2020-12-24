from typing import List, Union
from string import digits


def evaluate_line_task_1(line: str) -> int:
    line = line.replace(' ', '')
    value = 0
    number = 0
    action = '+'
    current_bracket_depth = 0
    bracket_str = ''
    for char in line:

        if char == ')':
            current_bracket_depth -= 1
            if not current_bracket_depth:
                number = evaluate_line_task_1(bracket_str)
                bracket_str = ''

        if current_bracket_depth:
            if char == '(':
                current_bracket_depth += 1
            bracket_str += char
            continue

        elif char in ['+', '*']:
            action = char
            continue
        elif char in digits:
            number = int(char)
        elif char == '(':
            current_bracket_depth += 1
            continue

        if action == '+':
            value += number
        elif action == '*':
            value *= number
    return value


def evaluate_line_task_2(line: str) -> int:
    line = line.replace(' ', '')

    # first group into characters, group brackets in one string
    segments: List[str] = []  # e.g. ['2', '*', '3', '+', '4*5']
    current_bracket_depth = 0
    bracket_str = ''
    for char in line:
        if char == '(':
            if current_bracket_depth:
                bracket_str += char
            current_bracket_depth += 1
            continue
        elif char == ')':
            current_bracket_depth -= 1
            if not current_bracket_depth:
                segments.append(bracket_str)
                bracket_str = ''
                continue
        if current_bracket_depth:
            bracket_str += char
        else:
            segments.append(char)

    # now evaluate parentheses
    cleaned_segments: List[Union[int, str]] = []  # e.g. [2(int), '*', 3, '+', 20]
    for char in segments:
        if len(char) == 1:
            value = int(char) if char in digits else char
            cleaned_segments.append(value)
        else:
            cleaned_segments.append(evaluate_line_task_2(char))

    # now evaluate additions
    addition_evaluated_segments: List[int] = []  # e.g. [2, 23]
    value = 0
    for segment in cleaned_segments:
        if isinstance(segment, int):
            value += segment
        elif segment == '*':
            addition_evaluated_segments.append(value)
            value = 0
    addition_evaluated_segments.append(value)

    multiplier = 1
    for value in addition_evaluated_segments:  # finally multiply everything left together
        multiplier *= value

    return multiplier


def task_1(lines: List[str]) -> int:
    accumulator = 0
    for line in lines:
        accumulator += evaluate_line_task_1(line)
    return accumulator


def task_2(lines: List[str]) -> int:
    accumulator = 0
    for line in lines:
        accumulator += evaluate_line_task_2(line)
    return accumulator


def main():
    lines = []
    for line in open('data/day_18.txt'):
        lines.append(line.replace('\n', ''))
    print(task_1(lines))
    print(task_2(lines))


if __name__ == '__main__':
    main()

