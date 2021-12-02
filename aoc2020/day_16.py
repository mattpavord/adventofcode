from typing import List, Tuple
from collections import OrderedDict
from copy import deepcopy


def load_data() -> Tuple[OrderedDict, List[int], List[List[int]]]:
    """
    :return:
    requirements_dict: E.g. {"departure track": [50, 150, 156, 950], ...}
        4 values represent the 4 boundaries in order of increased size
    my_ticket (List[int])
    other_tickets: list of tickets (list of lists of ints)
    """
    requirements_dict = OrderedDict()
    my_ticket = []
    other_tickets = []
    phase = 1
    for line in open('data/day_16.txt'):
        line = line.replace('\n', '')
        if not line:
            continue
        if 'ticket' in line:
            phase += 1
            continue
        if phase == 1:  # load requirements
            requirement, requirement_value = line.split(': ')
            r12, r34 = requirement_value.split(' or ')
            r1, r2 = [int(x) for x in r12.split('-')]
            r3, r4 = [int(x) for x in r34.split('-')]
            requirements_dict[requirement] = [r1, r2, r3, r4]
        if phase == 2:  # my ticket
            my_ticket = [int(x) for x in line.split(',')]
        if phase == 3:
            other_tickets.append([int(x) for x in line.split(',')])
    return requirements_dict, my_ticket, other_tickets


def task_1(requirements_dict: OrderedDict, other_tickets: List[List[int]]) -> int:
    accumulator = 0
    for ticket in other_tickets:
        for value in ticket:
            for r1, r2, r3, r4 in requirements_dict.values():
                if r1 <= value <= r2 or r3 <= value <= r4:
                    break  # number is valid
            else:  # number doesn't meet any requirements
                accumulator += value
    return accumulator


def task_2(requirements_dict: OrderedDict, my_ticket: List[int], other_tickets: List[List[int]]) -> int:

    # find invalid tickets
    invalid_tickets = []
    for i, ticket in enumerate(other_tickets):
        for value in ticket:
            for r1, r2, r3, r4 in requirements_dict.values():
                if r1 <= value <= r2 or r3 <= value <= r4:
                    break  # number is valid
            else:  # number doesn't meet any requirements
                invalid_tickets.append(i)

    # find potential positions for each requirement
    potential_positions = {}
    for requirement in requirements_dict:
        potential_positions[requirement] = list(range(len(my_ticket)))
    for j, ticket in enumerate(other_tickets):
        if j in invalid_tickets:
            continue
        for requirement, ranges in requirements_dict.items():
            r1, r2, r3, r4 = ranges
            for i, value in enumerate(ticket):
                valid = r1 <= value <= r2 or r3 <= value <= r4
                if not valid:
                    if i in potential_positions[requirement]:
                        potential_positions[requirement].remove(i)

    # organise potential positions
    actual_positions = {}  # requirement(str): position(int)
    while potential_positions:
        for requirement in deepcopy(potential_positions):
            for position in actual_positions.values():
                if position in potential_positions[requirement]:
                    potential_positions[requirement].remove(position)
            assert potential_positions[requirement]
            if len(potential_positions[requirement]) == 1:
                actual_positions[requirement] = potential_positions.pop(requirement)[0]

    # finally, add the departure values and return
    accumulator = 1
    for requirement, position in actual_positions.items():
        if "departure" in requirement:
            index = actual_positions[requirement]
            accumulator *= my_ticket[index]
    return accumulator


def main():
    requirements_dict, my_ticket, other_tickets = load_data()
    print(task_1(requirements_dict, other_tickets))
    print(task_2(requirements_dict, my_ticket, other_tickets))


if __name__ == '__main__':
    main()
