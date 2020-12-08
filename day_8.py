from typing import List, Tuple


def process_instruction(instruction: str, accumulator: int, index: int) -> Tuple[int, int]:
    """ Process instruction and modify accumulator and index appropriately """
    message, value = instruction.split(' ')
    value = int(value)
    if message == 'nop':
        index += 1
    if message == 'acc':
        index += 1
        accumulator += value
    if message == 'jmp':
        index += value
    return accumulator, index


def correct_and_run_instruction(instruction: str, accumulator: int, index: int) -> Tuple[int, int]:
    """
    Replace jmp with nop or vice versa, then run the instruction
    Raises Assertion error if instruction is acc
    """
    if instruction.split(' ')[0] == 'jmp':
        instruction = instruction.replace('jmp', 'nop')
    elif instruction.split(' ')[0] == 'nop':
        instruction = instruction.replace('nop', 'jmp')
    else:
        raise AssertionError("Invalid instruction to fix")
    return process_instruction(instruction, accumulator, index)


def task_1(instructions: List[str]) -> int:
    index = 0
    index_history = []
    accumulator = 0
    while index not in index_history:
        index_history.append(index)
        accumulator, index = process_instruction(instructions[index], accumulator, index)
    return accumulator


def task_2(instructions: List[str]) -> int:
    index = 0
    index_history = []
    accumulator = 0
    index_accumulator_history_map = {0: 0}  # index: accumulator

    # go until infinite loop
    while index not in index_history:
        index_history.append(index)
        accumulator, index = process_instruction(instructions[index], accumulator, index)
        index_accumulator_history_map[index] = accumulator

    reversed_index_history = index_history.copy()
    reversed_index_history.reverse()

    for index in reversed_index_history:
        accumulator = index_accumulator_history_map[index]
        starting_index = index
        new_index_history = index_history.copy()  # save history until infinite loop
        try:
            accumulator, index = correct_and_run_instruction(instructions[index], accumulator, index)
        except AssertionError:  # accumulator instruction found
            index_history.remove(starting_index)
            continue
        while index not in new_index_history:
            new_index_history.append(index)
            accumulator, index = process_instruction(instructions[index], accumulator, index)
            if index == len(instructions) - 1:
                accumulator, index = process_instruction(instructions[index], accumulator, index)
                return accumulator
        index_history.remove(starting_index)
    raise Exception("Could not find path")


def main():
    instructions = []
    for line in open('data/day_8.txt'):
        instructions.append(line.replace('\n', ''))
    print(task_1(instructions))
    print(task_2(instructions))


if __name__ == '__main__':
    main()
