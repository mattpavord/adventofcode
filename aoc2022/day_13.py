import json
from typing import Optional, Union


def compare(p1: Union[int, list], p2: Union[int, list]) -> Optional[bool]:
    """
    Returns True if correct order, False if not, None if identical
    """
    if p1 == p2:
        return None
    if isinstance(p1, int) and isinstance(p2, int):
        return p2 > p1
    if isinstance(p1, int):
        return compare([p1], p2)
    if isinstance(p2, int):
        return compare(p1, [p2])
    if p1 and not p2:
        return False
    if not p1 and p2:
        return True
    for i in range(max(len(p1), len(p2))):
        if len(p1) == i:
            return True
        if len(p2) == i:
            return False
        result = compare(p1[i], p2[i])
        if result is not None:
            return result


def task_1(data):
    total = 0
    for i, (p1, p2) in enumerate(data, start=1):
        if compare(p1, p2):
            total += i
    return total


def task_2(data):
    all_packets = []
    for row in data:
        all_packets.extend(row)

    # no need to sort all packets, only find which packets land before the divider packet
    output = 1
    divider_packets = [[[2]], [[6]]]  # important that these are in order for initial pos
    for pos, divider_packet in enumerate(divider_packets, start=1):
        for packet in all_packets:
            if compare(packet, divider_packet):
                pos += 1
        output *= pos
    return output


def main():
    data = []
    with open('data/day_13.txt', 'rt') as reader:
        raw_data = reader.read().split("\n\n")
    for pair in raw_data:
        data.append([json.loads(x) for x in pair.split("\n")])
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
