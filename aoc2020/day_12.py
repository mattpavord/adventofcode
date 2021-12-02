from typing import List, Tuple


DIRECTION_VECTORS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
DIRECTIONS = ['N', 'E', 'S', 'W']
TURN_INDEX_MAPPING = {'L': -1, 'R': 1}  # R goes forward one in the DIRECTIONS list, L goes back


class Ship:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def process_instruction(self, instruction: str):
        order = instruction[0]
        value = int(instruction[1:])

        if order in ['L', 'R']:
            assert value % 90 == 0
            n_rotations = value // 90
            current_direction_index = DIRECTIONS.index(self.direction)
            new_direction_index = (current_direction_index + n_rotations * TURN_INDEX_MAPPING[order]) % 4
            self.direction = DIRECTIONS[new_direction_index]

        else:
            direction_to_move = self.direction if order == 'F' else order
            dx, dy = DIRECTION_VECTORS[direction_to_move]
            self.x += dx * value
            self.y += dy * value


class WaypointShip:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.w_x = 10  # waypoint coords relative to ship
        self.w_y = 1

    def process_instruction(self, instruction: str):
        order = instruction[0]
        value = int(instruction[1:])

        if order in ['L', 'R']:
            assert value % 90 == 0
            n_rotations = value // 90
            turn_direction = TURN_INDEX_MAPPING[order]
            for _ in range(n_rotations):
                self.w_x, self.w_y = turn_direction * self.w_y, -1 * turn_direction * self.w_x

        elif order == 'F':
            self.x += self.w_x * value
            self.y += self.w_y * value

        else:
            dx, dy = DIRECTION_VECTORS[order]
            self.w_x += dx * value
            self.w_y += dy * value


def task_1(instructions: List[str]) -> int:
    ship = Ship(0, 0, 'E')
    for instruction in instructions:
        ship.process_instruction(instruction)
    return abs(ship.x) + abs(ship.y)


def task_2(instructions: List[str]) -> int:
    ship = WaypointShip(0, 0)
    for instruction in instructions:
        ship.process_instruction(instruction)
    return abs(ship.x) + abs(ship.y)


def main():
    instructions = []
    for line in open('data/day_12.txt'):
        instructions.append(line.replace('\n', ''))
    print(task_1(instructions))
    print(task_2(instructions))


if __name__ == '__main__':
    main()
