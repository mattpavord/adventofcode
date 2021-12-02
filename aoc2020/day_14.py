from typing import List


def convert_int_to_bits(n: int) -> str:
    """ Convert number into string of 36 binary 0 or 1 characters """
    binary_str = ""
    for i in range(36):
        char = '0'
        if n % (2**(i+1)):
            char = '1'
            n -= 2**i
        binary_str = char + binary_str
    return binary_str


def convert_bits_to_int(binary_str: str) -> int:
    """ Convert string binary into an integer """
    n = 0
    for i in range(len(binary_str)):
        if binary_str[-(i+1)] == '1':
            n += 2**i
    return n


def apply_mask_to_value(n: int, mask: str) -> int:
    binary_str = convert_int_to_bits(n)
    assert len(mask) == len(binary_str), "invalid mask"
    new_binary = []
    for i in range(len(mask)):
        new_binary.append(mask[i] if mask[i] != 'X' else binary_str[i])
    new_binary_str = "".join(new_binary)
    return convert_bits_to_int(new_binary_str)


def apply_mask_to_memory_value(n: int, mask: str) -> List[int]:
    """ Apply mask to a memory value, returns all combinations in int form """
    binary_str = convert_int_to_bits(n)
    assert len(mask) == len(binary_str), "invalid mask"
    new_binary = []
    for i in range(len(mask)):
        new_binary.append(mask[i] if mask[i] != '0' else binary_str[i])
    new_binary_str = "".join(new_binary)

    lowest_value = convert_bits_to_int(new_binary_str.replace('X', '0'))
    n_floating = new_binary_str.count('X')
    floating_values = [2**(35-pos) for pos, char in enumerate(new_binary_str) if char == 'X']
    floating_values.reverse()
    values = []
    for i in range(2**n_floating):
        value = lowest_value
        for j in range(n_floating):
            if i % (2 ** (j + 1)):
                value += floating_values[j]
                i -= 2 ** j
        values.append(value)
    return values


def task_1(instructions: List[str]) -> int:
    data = {}
    mask = None
    for instruction in instructions:
        action, value = instruction.split(' = ')
        if action == 'mask':
            mask = value
        else:
            value = int(value)
            index = int(action[4:].replace(']', ''))
            data[index] = apply_mask_to_value(value, mask)
    return sum(data.values())


def task_2(instructions: List[str]) -> int:
    data = {}
    mask = None
    for instruction in instructions:
        action, value = instruction.split(' = ')
        if action == 'mask':
            mask = value
        else:
            value = int(value)
            index = int(action[4:].replace(']', ''))
            indexes = apply_mask_to_memory_value(index, mask)
            for index in indexes:
                data[index] = value
    return sum(data.values())


def main():
    instructions = []
    for line in open('data/day_14.txt'):
        instructions.append(line.replace('\n', ''))
    print(task_1(instructions))
    print(task_2(instructions))


if __name__ == '__main__':
    main()
