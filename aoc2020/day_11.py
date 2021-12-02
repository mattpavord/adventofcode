from typing import Tuple

import numpy as np
from typing import List

# SEAT STATUS
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
ADJACENT_VECTORS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def convert_data_to_np_array(data: List[str]) -> np.array:
    np_data = np.zeros((len(data), len(data[0])), dtype=str)
    for i in range(len(data)):
        for j in range(len(data[0])):
            np_data[i, j] = data[i][j]
    return np_data


def determine_new_seat_status_adjacent(seating_plan: np.array, coordinates: Tuple[int, int]) -> str:
    """
    Given a seating plan and coordinates of a seat, return the new status of the seat
    Only checks adjacent seats
    """
    x, y = coordinates
    seat_status = seating_plan[x, y]
    if seat_status == FLOOR:
        return FLOOR
    n_adjacent_filled_seats = 0
    for dx, dy in ADJACENT_VECTORS:
        try:
            adjacent_seat_status = seating_plan[x + dx, y + dy]
            if x + dx < 0 or y + dy < 0:  # stop from wrapping around
                raise IndexError
        except IndexError:
            continue
        else:
            if adjacent_seat_status == OCCUPIED:
                n_adjacent_filled_seats += 1
    if seat_status == EMPTY and n_adjacent_filled_seats == 0:
        return OCCUPIED
    elif seat_status == OCCUPIED and n_adjacent_filled_seats >= 4:
        return EMPTY
    return seat_status


def determine_new_seat_status_los(seating_plan: np.array, coordinates: Tuple[int, int]) -> str:
    """
     Given a seating plan and coordinates of a seat, return the new status of the seat
     Checks all directions lines of sight
    """
    max_x, max_y = seating_plan.shape
    x, y = coordinates
    seat_status = seating_plan[x, y]
    if seat_status == FLOOR:
        return FLOOR

    n_filled_seats_seen = 0
    for dx, dy in ADJACENT_VECTORS:
        new_x, new_y = x + dx, y + dy
        while 0 <= new_x < max_x and 0 <= new_y < max_y:
            if seating_plan[new_x, new_y] == OCCUPIED:
                n_filled_seats_seen += 1
                break
            if seating_plan[new_x, new_y] == EMPTY:
                break
            new_x += dx
            new_y += dy

    if seat_status == EMPTY and n_filled_seats_seen == 0:
        return OCCUPIED
    elif seat_status == OCCUPIED and n_filled_seats_seen >= 5:
        return EMPTY
    return seat_status


def iterate_seating_plan(seating_plan: np.array, use_line_of_sight: bool = False) -> np.array:
    """ Iterate the seating arrangement, return next iteration """
    new_seating_plan = seating_plan.copy()
    max_x, max_y = seating_plan.shape
    for x in range(max_x):
        for y in range(max_y):
            if use_line_of_sight:
                new_seating_plan[x, y] = determine_new_seat_status_los(seating_plan, (x, y))
            else:
                new_seating_plan[x, y] = determine_new_seat_status_adjacent(seating_plan, (x, y))
    return new_seating_plan


def find_equilibrium_filled_seats(seating_plan: np.array, use_line_of_sight: bool = False) -> int:
    new_seating_plan = None
    while not np.array_equal(seating_plan, new_seating_plan):
        seating_plan = new_seating_plan if new_seating_plan is not None else seating_plan
        new_seating_plan = iterate_seating_plan(seating_plan, use_line_of_sight)
    return np.count_nonzero(seating_plan == OCCUPIED)


def task_1(seating_plan: np.array) -> int:
    return find_equilibrium_filled_seats(seating_plan)


def task_2(seating_plan: np.array) -> int:
    return find_equilibrium_filled_seats(seating_plan, use_line_of_sight=True)


def main():
    seating_plan = []
    for line in open('data/day_11.txt'):
        seating_plan.append(line.replace('\n', ''))
    seating_plan = convert_data_to_np_array(seating_plan)
    print(task_1(seating_plan))
    print(task_2(seating_plan))


if __name__ == '__main__':
    main()
