def check_safe(report: list[int]) -> bool:
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if not (all(d < 0 for d in diffs) or all(d > 0 for d in diffs)):
        return False
    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False
    return True


def task_1(data):
    safe_reports = 0
    for report in data:
        if check_safe(report):
            safe_reports += 1
    return safe_reports


def task_2(data):
    safe_reports = 0
    for report in data:
        if check_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                new_report = report.copy()
                new_report.pop(i)
                if check_safe(new_report):
                    safe_reports += 1
                    break
    return safe_reports


def main():
    with open('data/day_02.txt', 'rt') as reader:
        str_data = reader.read().split("\n")
    data = []
    for line in str_data:
        data.append([int(x) for x in line.split(" ")])
    print(task_1(data))
    print(task_2(data))


if __name__ == "__main__":
    main()
