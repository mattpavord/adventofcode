import os


def task_1(data):
    total = 0
    for inp, out in data:
        for code in out:
            if len(code) in [2, 3, 4, 7]:
                total += 1
    return total


def order(string):
    return ''.join([x for x in sorted(string)])


def calculate_digit_to_code_map(inp):
    inp = [order(code) for code in inp]
    digit_to_code_map = {}
    unique_length_map = {2: 1, 4: 4, 3: 7, 7: 8}
    # {unique_length: digit}

    # step 1 - get digits with unique lengths, 1, 4, 7 + 8
    for code in inp:
        if len(code) in unique_length_map:
            digit_to_code_map[unique_length_map[len(code)]] = code

    # step 2
    #   find 6, only digit with length 6 that does not encapsulate 1
    #   find 9, only digit with length 6 that encapsulates 4
    for code in inp:
        if len(code) == 6:
            if not all(x in code for x in digit_to_code_map[1]):
                digit_to_code_map[6] = code
            elif all(x in code for x in digit_to_code_map[4]):
                digit_to_code_map[9] = code

    # step 3 - find all other digits by unique traits
    #   0 is the only remaining 6 digit code
    #   of the remaining length 5s:
    #       5 is encapsulated by 6
    #       3 is encapsulated by 9
    for code in inp:
        if len(code) == 6 and code not in digit_to_code_map.values():
            digit_to_code_map[0] = code
        elif len(code) == 5:
            if all(x in digit_to_code_map[6] for x in code):
                digit_to_code_map[5] = code
            elif all(x in digit_to_code_map[9] for x in code):
                digit_to_code_map[3] = code

    # finally get 2 as only value not mapped yet
    diff = list(set(inp) - set(digit_to_code_map.values()))
    assert len(diff) == 1
    digit_to_code_map[2] = diff[0]

    return digit_to_code_map


def task_2(data):
    total = 0
    for inp, out in data:
        digit_to_code_map = calculate_digit_to_code_map(inp)
        code_to_digit_map = {v: k for k, v in digit_to_code_map.items()}
        digits = ''
        for code in out:
            digits += str(code_to_digit_map[order(code)])
        total += int(digits)
    return total


def main():
    data = []
    for line in open(os.getcwd() + '/data/day_08.txt'):
        line = line.replace('\n', '')
        inp, out = line.split(' | ')
        inp = inp.split(' ')
        out = out.split(' ')
        data.append((inp, out))
    print(task_1(data))
    print(task_2(data))


if __name__ == '__main__':
    main()
