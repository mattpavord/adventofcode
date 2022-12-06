from copy import deepcopy
import string
from collections import defaultdict


class Cargo:
    """
    Class to represent cargo
    Stack is a dict of {column: crates(list of chars)}
    E.g. {1: [N, Z]}
    First in list is top of crate
    """

    def __init__(self, stack):
        self.stack = stack

    def move_task_1(self, number, col_from, col_to):
        for _ in range(number):
            char = self.stack[col_from].pop(0)
            self.stack[col_to].insert(0, char)

    def move_task_2(self, number, col_from, col_to):
        for i in range(1, number + 1):
            char = self.stack[col_from].pop(number - i)
            self.stack[col_to].insert(0, char)


def execute_instructions(initial_stack, instructions, second_task=False):
    words_to_remove = ["move ", "from ", "to "]
    cargo = Cargo(initial_stack)
    for instruction in instructions:
        for word in words_to_remove:
            instruction = instruction.replace(word, "")
        number, col_from, col_to = [int(x) for x in instruction.split(" ")]
        if second_task:
            cargo.move_task_2(number, col_from, col_to)
        else:
            cargo.move_task_1(number, col_from, col_to)
    output = ""
    for col in sorted(cargo.stack.keys()):
        output += cargo.stack[col][0]
    return output


def task_1(initial_stack, instructions):
    return execute_instructions(initial_stack, instructions)


def task_2(initial_stack, instructions):
    return execute_instructions(initial_stack, instructions, second_task=True)


def main():
    initial_stack = defaultdict(list)
    instructions = []
    import_instructions = False
    for line in open("data/day_05.txt"):
        line = line.replace("\n", "")
        if not line:
            import_instructions = True
            continue
        if import_instructions:
            instructions.append(line)
        else:   # char is in the 4n-3 position
            for column in range(1, 10):  # max 9 columns
                try:
                    char = line[4 * column - 3]
                except IndexError:
                    continue
                else:
                    if char in string.ascii_uppercase:
                        initial_stack[column].append(char)

    print(task_1(deepcopy(initial_stack), instructions))
    print(task_2(deepcopy(initial_stack), instructions))


if __name__ == "__main__":
    main()
