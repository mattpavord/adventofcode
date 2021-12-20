import os

from string import ascii_lowercase


def get_other_element(ls, element):
    """ Given 2 element list, return other element """
    element_index = ls.index(element)
    other_element_index = {0: 1, 1: 0}[element_index]
    return ls[other_element_index]


def get_paths(data, path_so_far=None, part_2=False, double_visited=False):
    """ Return number of possible paths to end given the path of caves visited so far """

    if path_so_far is None:
        path_so_far = ["start"]
    current_cave = path_so_far[-1]
    if current_cave == "end":
        return 1

    possible_next_caves = []
    for passage in data:
        if current_cave in passage:
            neighbour_cave = get_other_element(passage, current_cave)
            small_cave = neighbour_cave[0] in ascii_lowercase
            if small_cave:
                if neighbour_cave not in path_so_far:
                    possible_next_caves.append(neighbour_cave)
                elif part_2 and neighbour_cave != "start" and not double_visited:
                    possible_next_caves.append(neighbour_cave)
            else:
                possible_next_caves.append(neighbour_cave)

    n_paths = 0
    for next_cave in possible_next_caves:
        double_visiting = (next_cave[0] in ascii_lowercase and next_cave in path_so_far) or double_visited
        n_paths += get_paths(data, path_so_far=path_so_far + [next_cave], part_2=part_2, double_visited=double_visiting)
    return n_paths


def task_1(data):
    return get_paths(data)


def task_2(data):
    return get_paths(data, part_2=True)


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_12.txt'):
        data.append(line.replace('\n', '').split('-'))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
