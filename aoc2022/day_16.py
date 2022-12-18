from typing import List
from dataclasses import dataclass


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


def track_path(valves):
    initial_optimisation = 10    # when paths get to this length, do a cull to help converge
    optimisation_steps = 5

    best_pressure_released = 0
    # path elements represent 1 minute each, id alone represents moving to there,
    # id* represents opening valve, e.g. [AA, DD, DD*], move from AA to DD, open DD
    paths_to_search = [["AA"]]
    while paths_to_search:
        if len(paths_to_search[0]) == initial_optimisation and len(paths_to_search[0]) < 30:
            # cull bottom 90% paths based on pressure_released
            paths_to_search = sorted(
                paths_to_search,
                key=lambda p: _determine_pressure_released(p, valves),
                reverse=True,
            )[: len(paths_to_search) // 10]
            initial_optimisation += optimisation_steps

        path = paths_to_search.pop(0)
        if len(path) == 30:
            pressure_released = _determine_pressure_released(path, valves)
            if pressure_released > best_pressure_released:
                best_pressure_released = pressure_released
        else:
            current_valve = valves[path[-1].replace("*", "")]
            if current_valve.flow_rate and current_valve.id + "*" not in path:
                paths_to_search.append(path + [current_valve.id + "*"])
            for valve_id in current_valve.tunnels:
                if len(path) >= 2 and valve_id == path[-2]:
                    continue  # no pointless returning
                paths_to_search.append(path + [valve_id])

    return best_pressure_released


def _determine_pressure_released(path, valves):
    """
    Given path, return the amount of pressure released after 30 mins
    If less than 30 elements are present, extrapolate at current rate
    """
    pressure_released = 0
    for time, valve_id in enumerate(path, start=1):
        if "*" in valve_id:
            valve = valves[valve_id[:-1]]
            pressure_released += valve.flow_rate * (31 - time)
    return pressure_released


def task_1(data):
    valves = init_valves(data)
    return track_path(valves)


def task_2(data):
    return


def main():
    with open("data/day_16.txt", "rt") as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
