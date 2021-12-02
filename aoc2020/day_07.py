from typing import Dict, List


def load_bag_rules() -> Dict:
    """
    Load bag rules in dictionary format as such
    {
        'bag_name_1': {'bag_contained': quantity, 'other_bag_contained': quantity, ...},
        ...,
    }
    """
    bag_rules = {}
    for line in open('data/day_7.txt'):
        line = line.replace('\n', '')
        rule_info = line.split(' ')
        bag = ' '.join(rule_info[:2])
        bag_rules[bag] = {}
        containing_bags_info = rule_info[4:]
        for i in range(len(containing_bags_info) // 4):
            containing_bag_info = containing_bags_info[4*i:4*(i+1)]
            quantity = int(containing_bag_info[0])
            containing_bag = ' '.join(containing_bag_info[1:3])
            bag_rules[bag][containing_bag] = quantity
    return bag_rules


def find_direct_containing_bags(bag: str, bag_rules: Dict) -> List[str]:
    """
    Given a bag name, return a list of strings that can directly contain this bag from the bag rules
    """
    containing_bags = []
    for containing_bag, contained_bags in bag_rules.items():
        if bag in contained_bags:
            containing_bags.append(containing_bag)
    return containing_bags


def find_number_of_contained_bags(bag: str, bag_rules: Dict) -> int:
    """ Find number of bags that are contained in bag input"""
    if bag not in bag_rules:
        return 0
    n_contained_bags = 0
    for contained_bag, quantity in bag_rules[bag].items():
        n_contained_bags += quantity + quantity * find_number_of_contained_bags(contained_bag, bag_rules)
    return n_contained_bags


def task_1(bag_rules: Dict) -> int:
    containing_bags = find_direct_containing_bags('shiny gold', bag_rules)
    all_containing_bags = []  # includes all recursions
    while containing_bags:
        all_containing_bags.extend(containing_bags)
        next_recursion_of_containing_bags = []
        for containing_bag in containing_bags:
            next_recursion_of_containing_bags.extend(find_direct_containing_bags(containing_bag, bag_rules))
        containing_bags = list(set(next_recursion_of_containing_bags))  # remove duplicates
    return len(set(all_containing_bags))


def task_2(bag_rules: Dict) -> int:
    return find_number_of_contained_bags('shiny gold', bag_rules)


def main():
    bag_rules = load_bag_rules()
    print(task_1(bag_rules))
    print(task_2(bag_rules))


if __name__ == '__main__':
    main()
