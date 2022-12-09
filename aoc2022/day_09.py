import numpy as np


def move_rope(data, rope_length):
    rope_positions = [
        np.array((0, 0)) for _ in range(rope_length)
    ]  # first array is head of rope
    tail_positions = [(0, 0)]
    direction_vector_map = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    adjacent_moves = list(direction_vector_map.values())
    diagonal_moves = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    for line in data:
        direction, magnitude = line.split(" ")
        for _ in range(int(magnitude)):

            rope_positions[0] += np.array(direction_vector_map[direction])
            for i in range(1, rope_length):
                if np.linalg.norm(rope_positions[i - 1] - rope_positions[i]) > 1.42:  # ~ root 2

                    if (  # if on same column or row move adjacent
                        rope_positions[i][0] == rope_positions[i - 1][0]
                        or rope_positions[i][1] == rope_positions[i - 1][1]
                    ):
                        possible_moves = adjacent_moves
                    else:  # otherwise move diagonally
                        possible_moves = diagonal_moves

                    difference_vector = rope_positions[i-1] - rope_positions[i]
                    # select closest vector
                    move = max(possible_moves, key=lambda x: np.dot(x, difference_vector))
                    rope_positions[i] += move

            tail_positions.append(tuple(rope_positions[-1]))  # save final tail position

    return len(set(tail_positions))


def task_1(data):
    return move_rope(data, 2)


def task_2(data):
    return move_rope(data, 10)


def main():
    with open("data/day_09.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
