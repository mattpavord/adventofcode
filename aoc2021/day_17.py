import os


def task_1(data):
    """
    We want max y velocity that will land in target area,
    When y comes back down at point 0, it will have the same magnitude of velocity
    it started with, but negative
    Ignore x as we can give it a slow speed that will always land in area
    Max y speed must therefore be -1 * y_min - 1 to get in range with one iteration
    Note that this assumes y_min is negative
    """
    y_min = data[1][0]
    v_y = -1 * y_min - 1
    y = 0
    while v_y > 0:
        y += v_y
        v_y -= 1
    return y


def task_2(data):
    """
    Solve this problem by making maps of {v_x: [n_iterations]} and {v_y: [n_iterations]}
    n_iterations are in lists as there could be more than one
    in case of x - if probe stops in range then the possible_iterations value will be
    {v_x: [5 '+'] indicating that n_iterations >= 5
    Note this assumes y_range is negative and x_range is positive
    """
    [x_min, x_max], [y_min, y_max] = data

    # evaluate x_speeds
    x_speeds = {}
    max_x_speed = x_max
    for starting_x_speed in range(1, max_x_speed + 1):
        possible_iterations = []
        v_x = starting_x_speed
        n_iterations = 0
        x = 0
        while v_x > 0 and x <= x_max:
            x += v_x
            v_x -= 1
            n_iterations += 1
            if x_min <= x <= x_max:
                possible_iterations.append(n_iterations)
        if x_min <= x <= x_max:
            possible_iterations = [possible_iterations[0], '+']
        if possible_iterations:
            x_speeds[starting_x_speed] = possible_iterations

    # evaluate y speeds
    y_speeds = {}
    max_y_speed = -1 * y_min
    min_y_speed = -1 * max_y_speed
    for starting_y_speed in range(min_y_speed, max_y_speed + 1):
        possible_iterations = []
        v_y = starting_y_speed
        n_iterations = 0
        y = 0
        while y >= y_min:
            y += v_y
            v_y -= 1
            n_iterations += 1
            if y_min <= y <= y_max:
                possible_iterations.append(n_iterations)
        if possible_iterations:
            y_speeds[starting_y_speed] = possible_iterations

    # combine
    velocities = []
    for v_x, poss_x_iterations in x_speeds.items():
        for v_y, poss_y_iterations in y_speeds.items():
            if set(poss_x_iterations).intersection(set(poss_y_iterations)):
                velocities.append((v_x, v_y))
            elif '+' in poss_x_iterations:
                if max(poss_y_iterations) >= poss_x_iterations[0]:
                    velocities.append((v_x, v_y))

    return len(velocities)


def main():
    data = ''
    for line in open(os.getcwd() + '/data/day_17.txt'):
        data = line.replace('\n', '')
    data = data[13:].split(', ')
    x_range = [int(x) for x in data[0][2:].split('..')]
    y_range = [int(x) for x in data[1][2:].split('..')]
    data = [x_range, y_range]
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
