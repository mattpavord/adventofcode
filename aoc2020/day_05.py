from typing import List, Tuple


def convert_code_to_row_and_column(code: str) -> Tuple[int, int]:
    row_code = code[:7]
    column_code = code[7:]
    row_number = column_number = 0
    for i in range(len(row_code)):
        digit = row_code[-(i+1)]  # go from back to front
        if digit == 'B':
            row_number += 2 ** i
    for i in range(len(column_code)):
        digit = column_code[-(i+1)]  # go from back to front
        if digit == 'R':
            column_number += 2 ** i
    return row_number, column_number


def get_seat_ids(boarding_passes: List[str]) -> List[int]:
    seat_ids = []
    for code in boarding_passes:
        row, column = convert_code_to_row_and_column(code)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    return seat_ids


def task_1(boarding_passes: List[str]) -> int:
    seat_ids = get_seat_ids(boarding_passes)
    return max(seat_ids)


def task_2(boarding_passes: List[str]) -> int:
    possible_seat_ids = []
    seat_ids = set(get_seat_ids(boarding_passes))
    for number in range(min(seat_ids), max(seat_ids)):
        if (number + 1) in seat_ids and (number - 1) in seat_ids and number not in seat_ids:
            possible_seat_ids.append(number)
    assert len(possible_seat_ids) == 1, "Found multiple matches"
    return possible_seat_ids[0]


def main():
    boarding_passes = []
    for line in open('data/day_5.txt'):
        boarding_passes.append(line.replace('\n', ''))
    print(task_1(boarding_passes))
    print(task_2(boarding_passes))


if __name__ == '__main__':
    main()
