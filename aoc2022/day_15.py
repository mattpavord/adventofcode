def calculate_n_occupied(data, y_coord):
    occupied_x_coords = set()
    for (s_x, s_y), (b_x, b_y) in data:
        m_distance = abs(b_x - s_x) + abs(b_y - s_y)
        sensor_distance_to_y_coord = abs(y_coord - s_y)
        remaining_distance = m_distance - sensor_distance_to_y_coord
        x_min = s_x - remaining_distance
        x_max = s_x + remaining_distance
        occupied_x_coords = occupied_x_coords | set(range(x_min, x_max))
    return len(occupied_x_coords)


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
