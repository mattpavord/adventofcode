import os
from collections import defaultdict


def iterate_polymer(polymer, rules, n_iterations):

    double_counted_letters = defaultdict(int)
    for c in polymer:  # everything counted twice except first and last
        double_counted_letters[c] = polymer.count(c)
    double_counted_letters[polymer[0]] -= 1
    double_counted_letters[polymer[-1]] -= 1
    rule_pairs = {rule[0]: [rule[0][0] + rule[1], rule[1] + rule[0][1]] for rule in rules}
    pair_quantities = defaultdict(int)

    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        if pair in rule_pairs.keys():
            pair_quantities[pair] += 1
        else:
            raise AssertionError("Assumption that all possible pairs are in rules not valid")

    # iterate each pair
    for _ in range(n_iterations):
        next_pair_quantities = defaultdict(int)
        for pair, quantity in pair_quantities.items():
            next_pairs = rule_pairs[pair]
            for next_pair in next_pairs:
                if next_pair not in rule_pairs.keys():
                    raise AssertionError("Assumption that all possible pairs are in rules not valid")
                next_pair_quantities[next_pair] += quantity
            added_char = next_pairs[0][1]
            double_counted_letters[added_char] += quantity
        pair_quantities = next_pair_quantities

    # finally count characters
    char_count = defaultdict(int)
    for pair, quantity in pair_quantities.items():
        char_count[pair[0]] += quantity
        char_count[pair[1]] += quantity
    for char, value in double_counted_letters.items():
        char_count[char] -= value
    char_quantities = list(char_count.values())
    char_quantities = sorted(char_quantities)
    return char_quantities[-1] - char_quantities[0]


def task_1(polymer, rules):
    return iterate_polymer(polymer, rules, 10)


def task_2(polymer, rules):
    return iterate_polymer(polymer, rules, 40)


def main():
    polymer = ''
    rules = []
    for line in open(os.getcwd() + '/data/day_14.txt'):
        line = line.replace('\n', '')
        if not line:
            continue
        elif '->' in line:
            rules.append(line.split(' -> '))
        else:
            polymer = line
    print(task_1(polymer, rules))
    print(task_2(polymer, rules))


if __name__ == '__main__':
    main()