def calculate_n_occupied(data, y_coord):
    x_ranges = []  # determine start and stop values
    for (s_x, s_y), (b_x, b_y) in data:
        m_distance = abs(b_x - s_x) + abs(b_y - s_y)
        sensor_distance_to_y_coord = abs(y_coord - s_y)
        remaining_distance = m_distance - sensor_distance_to_y_coord
        if remaining_distance < 0:
            continue
        x_min = s_x - remaining_distance
        x_max = s_x + remaining_distance
        x_ranges.append((x_min, x_max))
    x_ranges = sorted(x_ranges, key=lambda r: r[0])

    # combine ranges so no overlap
    overlap = True
    while overlap:
        new_x_ranges = []
        for i in range(len(x_ranges) - 1):
            x_min_1, x_max_1 = x_ranges[i]
            x_min_2, x_max_2 = x_ranges[i+1]
            if x_min_2 <= x_max_1:
                new_x_ranges.append((x_min_1, max(x_max_1, x_max_2)))
                # let's not overcomplicate - start over with new ranges
                new_x_ranges.extend(x_ranges[i+2:])
                break
            else:
                new_x_ranges.append((x_min_1, x_max_1))
        else:
            overlap = False
        if overlap:
            x_ranges = new_x_ranges.copy()

    return sum([x_max - x_min for x_min, x_max in x_ranges])


def task_1(data):
    return calculate_n_occupied(data, y_coord=2000000)


def task_2(data):
    return


def main():
    with open('data/day_15.txt', 'rt') as reader:
        raw_data = reader.read().split("\n")
    data = []
    for line in raw_data:
        line = line.split(" ")
        s_x = int(line[2][2:-1])
        s_y = int(line[3][2:-1])
        b_x = int(line[8][2:-1])
        b_y = int(line[9][2:])
        data.append([(s_x, s_y), (b_x, b_y)])
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
