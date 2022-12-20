import numpy as np


def init_blueprints(data):
    blueprints = []
    # each blueprint is a 4x4 np.array, consisting of each robot, and it's cost
    # in order (ore, clay, obsidian, geode)
    for line in data:
        blueprint = np.zeros((4, 4), dtype=int)
        line = line.split(" ")
        blueprint[0, 0] = int(line[6])
        blueprint[1, 0] = int(line[12])
        blueprint[2, 0] = int(line[18])
        blueprint[2, 1] = int(line[21])
        blueprint[3, 0] = int(line[27])
        blueprint[3, 2] = int(line[30])
        blueprints.append(blueprint)
    return blueprints


def simulate_max_geodes(blueprint):
    paths_to_search = ["."]
    # . represents do nothing, 0, 1, 2, 3 represents build robot (ore, clay, obsidian, geode)
    paths_searched = set(paths_to_search)
    most_geodes = 0
    optimise_at_path_length = 15
    while paths_to_search:
        if len(paths_to_search[0]) == optimise_at_path_length:
            n_paths_to_search = len(paths_to_search)
            paths_to_search = _optimise(paths_to_search, blueprint)
            # print(f"Optimising at step {len(paths_to_search[0])} from "
            #       f"{n_paths_to_search} to {len(paths_to_search)}")
            optimise_at_path_length += 1

        path = paths_to_search.pop(0)
        rocks_collected, robots_built = _determine_status(path, blueprint)
        if len(path) == 24:
            if rocks_collected[3] > most_geodes:
                print(path)
                most_geodes = rocks_collected[3]
        else:
            for i, robot_cost in enumerate(blueprint):
                possible_next_steps = ["."]
                if all(np.greater_equal(rocks_collected, robot_cost)):
                    possible_next_steps.append(str(i))
                if "3" in possible_next_steps:  # always build a geode robot if possible
                    possible_next_steps = ["3"]
                for step in possible_next_steps:
                    new_path = path + step
                    if new_path not in paths_searched:
                        paths_to_search.append(new_path)
                        paths_searched.add(new_path)
    return most_geodes


def _optimise(paths_to_search, blueprint):
    """More shady optimising strategies, yay!"""
    return sorted(
        paths_to_search,
        key=lambda p: _score_path(p, blueprint),
        reverse=True,
    )[:2000]


def _score_path(path, blueprint):
    """
    For a given incomplete path, give a path a score based on the estimated number of
    obsidian and geode rocks it can produce
    """
    rocks, robots = _determine_status(path, blueprint)
    geode_robot_cost = blueprint[3]
    for _ in range(24 - len(path)):
        if all(np.greater_equal(rocks, geode_robot_cost)):
            rocks += robots
            robots[3] += 1
            rocks -= geode_robot_cost
        else:
            rocks += robots
    return rocks[3] * 100 + rocks[2]


def _determine_status(path, blueprint):
    """Determine rocks collected and robots built for a path"""
    robots = np.array([1, 0, 0, 0])
    rocks = np.array([0, 0, 0, 0])
    for char in path:
        rocks += robots
        if char in "0123":
            robot_id = int(char)
            robots[robot_id] += 1
            rocks -= blueprint[robot_id]
    return rocks, robots


def task_1(data):
    blueprints = init_blueprints(data)
    output = 0
    for i, blueprint in enumerate(blueprints, start=1):
        max_geodes = simulate_max_geodes(blueprint)
        output += max_geodes * i
        print(f"Blueprint {i} produced {max_geodes} geodes\n")
    return output


def task_2(data):
    return


def main():
    with open("data/day_19.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
