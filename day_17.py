from typing import Set, List


def get_starting_active_cubes(data: List[str], four_dimensions: bool = False) -> Set[tuple]:
    """
    Returns active coordinates in a set {(x,y,z), ...}
    """
    active_cubes = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                if four_dimensions:
                    active_cubes.add((x, y, 0, 0))
                else:
                    active_cubes.add((x, y, 0))
    return active_cubes


def iterate_3d(active_cubes: Set[tuple]) -> Set[tuple]:
    """ Iterate active cubes once """
    neighbours = (-1, 0, 1)
    neighbours_to_active_cubes = {}  # {coordinate_tuple: number of active neighbours}
    for x, y, z in active_cubes:
        for i in neighbours:
            for j in neighbours:
                for k in neighbours:
                    if not (i or j or k):
                        continue
                    new_coords = (x+i, y+j, z+k)
                    if new_coords in neighbours_to_active_cubes:
                        neighbours_to_active_cubes[new_coords] += 1
                    else:
                        neighbours_to_active_cubes[new_coords] = 1

    new_active_cubes = set()
    for coords, n_active_neighbours in neighbours_to_active_cubes.items():
        if n_active_neighbours == 3 or (coords in active_cubes and n_active_neighbours == 2):
            new_active_cubes.add(coords)
    return new_active_cubes


def iterate_4d(active_cubes: Set[tuple]) -> Set[tuple]:
    """ Iterate active cubes once """
    neighbours = (-1, 0, 1)
    neighbours_to_active_cubes = {}  # {coordinate_tuple: number of active neighbours}
    for x, y, z, w in active_cubes:
        for i in neighbours:
            for j in neighbours:
                for k in neighbours:
                    for l in neighbours:
                        if not (i or j or k or l):  # make sure we are not checking self
                            continue
                        new_coords = (x+i, y+j, z+k, w+l)
                        if new_coords in neighbours_to_active_cubes:
                            neighbours_to_active_cubes[new_coords] += 1
                        else:
                            neighbours_to_active_cubes[new_coords] = 1

    new_active_cubes = set()
    for coords, n_active_neighbours in neighbours_to_active_cubes.items():
        if n_active_neighbours == 3 or (coords in active_cubes and n_active_neighbours == 2):
            new_active_cubes.add(coords)
    return new_active_cubes


def task_1(start_data: List[str]):
    active_cubes = get_starting_active_cubes(start_data)
    for _ in range(6):
        active_cubes = iterate_3d(active_cubes)
    return len(active_cubes)


def task_2(start_data: List[str]):
    active_cubes = get_starting_active_cubes(start_data, four_dimensions=True)
    for _ in range(6):
        active_cubes = iterate_4d(active_cubes)
    return len(active_cubes)


def main():
    data = []
    for line in open('data/day_17.txt'):
        data.append(line.replace('\n', ''))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()

