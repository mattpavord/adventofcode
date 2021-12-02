from typing import List

# jolt_numbers refers to the full input list
# snippet refers to a subset of jolt_numbers


def organise_jolt_numbers(jolt_numbers: List[int]) -> None:
    """ Sort jolt numbers and add first and last requirements """
    jolt_numbers.sort()
    jolt_numbers.append(jolt_numbers[-1] + 3)
    jolt_numbers.insert(0, 0)


def find_snippet_combinations(snippet: List[int]) -> int:
    """
    Given an ordered list, find the number of combinations of the snippet by removing values without making the max
    difference greater than 3, do not remove the first and last value

    This is a bit cheaty but I've spent too long on this now:
        Snippet must be of length 5 or less
        Snippets of length 4 or 5 must not have a difference greater than 1

    :param snippet: Ordered list
    :return: n_combinations(int)
    """
    if len(snippet) <= 2:  # cannot
        return 1
    if len(snippet) == 3:
        return 2 if snippet[2] - snippet[0] <= 3 else 1

    assert len(snippet) <= 5
    assert max([snippet[i+1] - snippet[i] for i in range(len(snippet)-1)]) == 1

    n_combinations_per_length = {4: 4, 5: 7}
    return n_combinations_per_length[len(snippet)]


def task_1(jolt_numbers: List[int]) -> int:
    organise_jolt_numbers(jolt_numbers)
    n_differences = {1: 0, 2: 0, 3: 0}  # {difference: occurrence of difference}
    for i in range(len(jolt_numbers) - 1):
        difference = jolt_numbers[i + 1] - jolt_numbers[i]
        n_differences[difference] += 1
    return n_differences[1] * n_differences[3]


def task_2(jolt_numbers: List[int]) -> int:
    organise_jolt_numbers(jolt_numbers)
    compulsary_numbers = {0}  # numbers that are next to a 3-gap, therefore we cannot remove
    for i in range(len(jolt_numbers) - 1):
        difference = jolt_numbers[i + 1] - jolt_numbers[i]
        if difference == 3:
            compulsary_numbers.add(jolt_numbers[i])
            compulsary_numbers.add(jolt_numbers[i + 1])

    # sort into 'snippets', each starting and ending with a compulsary number, no compulsary numbers in the middle
    snippets: List[List[int]] = []
    current_snippet = []
    for number in jolt_numbers:
        if number in compulsary_numbers:
            current_snippet.append(number)
            snippets.append(current_snippet)
            current_snippet = [number]
        else:
            current_snippet.append(number)
    snippets.append(current_snippet)

    # work out how many combinations in each snippet
    n_combinations = 1
    for snippet in snippets:
        n_combinations *= find_snippet_combinations(snippet)

    return n_combinations


def main():
    jolt_numbers = []
    for line in open('data/day_10.txt'):
        jolt_numbers.append(int(line.replace('\n', '')))
    print(task_1(jolt_numbers))
    print(task_2(jolt_numbers))


if __name__ == '__main__':
    main()
