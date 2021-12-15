import os


BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}
TASK_1_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
TASK_2_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


def task_1(data):
    total = 0
    for line in data:
        current_brackets = []
        for bracket in line:
            if bracket in BRACKETS.keys():
                current_brackets.append(bracket)
            else:
                prev_open_bracket = current_brackets.pop(-1)
                if BRACKETS[prev_open_bracket] != bracket:
                    total += TASK_1_POINTS[bracket]
                    break
    return total


def task_2(data):
    scores = []
    for line in data:
        current_brackets = []
        for bracket in line:
            if bracket in BRACKETS.keys():
                current_brackets.append(bracket)
            else:
                prev_open_bracket = current_brackets.pop(-1)
                if BRACKETS[prev_open_bracket] != bracket:
                    break
        else:  # line is not corrupted
            current_brackets.reverse()
            closing_brackets = [BRACKETS[x] for x in current_brackets]
            score = 0
            for bracket in closing_brackets:
                score = score * 5 + TASK_2_POINTS[bracket]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_10.txt'):
        data.append(line.replace('\n', ''))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
