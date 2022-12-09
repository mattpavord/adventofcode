import numpy as np


def task_1(data):
    current_head_pos = np.array((0, 0))
    tail_positions = [(0, 0)]
    direction_vector_map = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for line in data:
        direction, magnitude = line.split(" ")
        for _ in range(int(magnitude)):
            new_head_pos = current_head_pos + np.array(direction_vector_map[direction])
            tail_pos = np.array(tail_positions[-1])
            if np.linalg.norm(new_head_pos - tail_pos) > 1.42:  # roughly root 2
                # tail moves to prev head pos
                tail_positions.append(tuple(current_head_pos))  # use tuple as hashable for set

            current_head_pos = new_head_pos

    return len(set(tail_positions))


def task_2(data):
    return


def main():
    with open('data/day_09.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
