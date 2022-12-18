from typing import Dict, List, Tuple
from dataclasses import dataclass
import itertools


@dataclass
class Valve:
    id: str
    flow_rate: int
    tunnels: List[str]


def init_valves(data):
    valves = {}
    for line in data:
        line = line.split(" ")
        valve = Valve(
            id=line[1],
            flow_rate=int(line[4].replace("rate=", "")[:-1]),
            tunnels=[t.replace(",", "") for t in line[9:]],
        )
        valves[valve.id] = valve
    return valves


def track_path(valves, n_entities, max_time, initial_optimisation=10, optimisation_steps=5):

    best_pressure_released = 0
    # path elements represent 1 minute each, id alone represents moving to there,
    # id* represents opening valve, e.g. [("AA"), ("DD"), ("DD*")], move from AA to DD, open DD
    # use a tuple to represent different track entities for part 2
    paths_to_search = [[("AA",) * n_entities]]
    while paths_to_search:
        # print(len(paths_to_search), len(paths_to_search[0]))

        # optimisation - cull bottom 90% paths based on pressure_released
        if (
                len(paths_to_search[0]) == initial_optimisation
                and len(paths_to_search[0]) < max_time
                and len(paths_to_search) > 50
        ):
            paths_to_search = sorted(
                paths_to_search,
                key=lambda p: _determine_pressure_released(p, valves, max_time),
                reverse=True,
            )[: len(paths_to_search) // 10]
            print("Optimising", initial_optimisation, len(paths_to_search))
            initial_optimisation += optimisation_steps

        path = paths_to_search.pop(0)
        if len(path) == max_time:
            pressure_released = _determine_pressure_released(path, valves, max_time)
            if pressure_released > best_pressure_released:
                best_pressure_released = pressure_released
        else:
            possible_next_valves = _determine_possible_next_valves(path, valves)
            for step in itertools.product(*possible_next_valves):
                # ensure we don't open the same valve more than once
                if len(step) > 1 and step[0] == step[1] and "*" in step[0]:
                    continue
                paths_to_search.append(path + [tuple(step)])

    return best_pressure_released


def _determine_pressure_released(path, valves, max_time):
    """
    Given path, return the amount of pressure released after 30 mins
    If less than 30 elements are present, extrapolate at current rate
    """
    pressure_released = 0
    for time, valve_ids in enumerate(path, start=1):
        for valve_id in valve_ids:
            if "*" in valve_id:
                valve = valves[valve_id[:-1]]
                pressure_released += valve.flow_rate * (max_time + 1 - time)
    return pressure_released


def _determine_possible_next_valves(
        path: List[Tuple[str]], valves: Dict[str, Valve]
) -> List[List[str]]:
    n_entities = len(path[0])
    current_valve_ids = [v.replace("*", "") for v in path[-1]]
    opened_valves = _determine_opened_valves(path)
    possible_next_valves = [[] for _ in range(n_entities)]
    for i, current_valve_id in enumerate(current_valve_ids):
        current_valve = valves[current_valve_id]
        if current_valve.flow_rate and current_valve_id not in opened_valves:
            possible_next_valves[i].append(current_valve.id + "*")
        for valve_id in current_valve.tunnels:
            if len(path) >= 2 and valve_id == path[-2][i]:
                continue  # no pointless returning
            possible_next_valves[i].append(valve_id)
    return possible_next_valves


def _determine_opened_valves(path):
    opened_valves = []
    for step in path:
        for valve in step:
            if "*" in valve:
                opened_valves.append(valve.replace("*", ""))
    return opened_valves


def task_1(data):
    valves = init_valves(data)
    return track_path(valves, 1, 30)


def task_2(data):
    valves = init_valves(data)
    return track_path(valves, 2, 26, initial_optimisation=8, optimisation_steps=2)


def main():
    with open("data/day_16.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
