import os


POINT_MAPPING = {"A": 1, "B": 2, "C": 3}
WINNING_ORDER = ["A", "C", "B", "A"]  # shape beats the shape one index ahead of itself


def points_awarded(opponent, own):
    """
    opponent and own are two characters in the set ("A", "B", "C") representing the opponents
    choice and our own choice
    """
    points = POINT_MAPPING[own]
    if opponent == own:
        points += 3  # draw
    elif WINNING_ORDER[WINNING_ORDER.index(own) + 1] == opponent:
        points += 6  # win
    return points


def task_1(data):
    shape_mapping = {"X": "A", "Y": "B", "Z": "C"}
    return sum(
        points_awarded(match.split(" ")[0], shape_mapping[match.split(" ")[1]])
        for match in data
    )


def task_2(data):
    total = 0
    for match in data:
        opponent, outcome = match.split(" ")
        own = {
            "X": WINNING_ORDER[WINNING_ORDER.index(opponent) + 1],
            "Y": opponent,
            "Z": WINNING_ORDER[WINNING_ORDER.index(opponent, 1) - 1]
        }[outcome]
        total += points_awarded(opponent, own)
    return total


def main():
    data = []
    for line in open(os.getcwd() + "/data/day_02.txt"):
        data.append(line.replace("\n", ""))

    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
