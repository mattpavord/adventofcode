from typing import List


def task_1(available_time: int, bus_ids: List[int]) -> int:
    depart_time = available_time
    while True:
        for bus_id in bus_ids:
            if not depart_time % bus_id:  # check if depart_time is a multiple of bus_id
                return (depart_time - available_time) * bus_id
        depart_time += 1


def task_2(schedule: List[str]) -> int:
    timestamp = accumulator = 1
    for i in range(len(schedule)):
        if schedule[i] == 'x':
            continue
        while (timestamp + i) % int(schedule[i]):  # check if timestamp is a multiple
            timestamp += accumulator
        accumulator *= int(schedule[i])  # make sure that we maintain all solutions of the previous numbers
    return timestamp


def main():
    data = []
    for line in open('data/day_13.txt'):
        data.append(line.replace('\n', ''))
    available_time = int(data[0])
    bus_ids = [int(n) for n in data[1].split(',') if n != 'x']
    schedule = data[1].split(',')  # keep x for part 2
    print(task_1(available_time, bus_ids))
    print(task_2(schedule))


if __name__ == '__main__':
    main()
