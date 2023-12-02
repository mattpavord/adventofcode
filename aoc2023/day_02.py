def task_1(data):
    total = 0
    for line in data:
        max_color = {"red": 0, "green": 0, "blue": 0}
        game_data, color_data = line.split(": ")
        game_id = int(game_data.split(" ")[1])
        for colors in color_data.split("; "):
            for color in colors.split(", "):
                number, color = color.split(" ")
                number = int(number)
                if number > max_color[color]:
                    max_color[color] = number
        if max_color["red"] <= 12 and max_color["green"] <= 13 and max_color["blue"] <= 14:
            total += game_id
    return total


def task_2(data):
    total = 0
    for line in data:
        max_color = {"red": 0, "green": 0, "blue": 0}
        game_data, color_data = line.split(": ")
        for colors in color_data.split("; "):
            for color in colors.split(", "):
                number, color = color.split(" ")
                number = int(number)
                if number > max_color[color]:
                    max_color[color] = number
        total += max_color["red"] * max_color["green"] * max_color["blue"]
    return total


def main():
    with open('data/day_02.txt', 'rt') as reader:
        data = reader.read().split("\n")
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
