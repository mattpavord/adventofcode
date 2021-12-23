import os

from pprint import pprint


def convert_hexadecimal_to_bits(hexadecimal):
    hex_to_bit = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    output = ''
    for char in hexadecimal:
        output += hex_to_bit[char]
    return output


def binary_to_int(binary):
    output = 0
    for i in range(len(binary)):
        output += int(binary[-1*(i+1)]) * 2**i
    return output


def product(numbers):
    assert numbers
    x = 1
    for n in numbers:
        x *= n
    return x


def gt(numbers):
    assert len(numbers) == 2
    return 1 if numbers[0] > numbers[1] else 0


def lt(numbers):
    assert len(numbers) == 2
    return 1 if numbers[0] < numbers[1] else 0


def eq(numbers):
    assert len(numbers) == 2
    return 1 if numbers[0] == numbers[1] else 0


def evaluate_operator_values(packets):
    operation_map = {0: sum, 1: product, 2: min, 3: max, 5: gt, 6: lt, 7: eq}
    for k in range(len(packets)):
        packet = packets[-1*(k+1)]
        if packet["packet_type"] == 4:
            continue
        operation = operation_map[packet["packet_type"]]
        numbers = [x["value"] for x in packets if x["parent_operator_id"] == packet["operator_id"]]
        try:
            packet["value"] = operation(numbers)
        except AssertionError as e:
            print(numbers, packet["operator_id"])
            raise e


def scan_hexadecimal(hexadecimal):
    """
    Returns a list of dicts containing packet information
    {
        "version": <int>
        "packet_type": <int>
        "value": Optional[int] (None if not literal_value)
        "parent_operator_id": Optional[int] id of operator containing packet
        "operator_id": Optional[int] id of operator
        "starting_index": index of bits where packet starts
    }
    """
    bits = convert_hexadecimal_to_bits(hexadecimal)
    packets = []
    i = 0
    operator_id = 1

    # first decode the basics into JSON, - literal values, packet_type, versions
    while i < len(bits.strip('0')):  # i should be the first index of a new packet
        version = binary_to_int(bits[i: i+3])
        packet_type = binary_to_int(bits[i+3:i+6])
        packet = {
            "version": version,
            "packet_type": packet_type,
            "starting_index": i,
            "value": None,
        }

        if packet_type == 4:  # literal value
            value_bits = ''
            i += 6
            while bits[i] == '1':
                value_bits += bits[i+1: i+5]
                i += 5
            value_bits += bits[i+1: i+5]  # get final one
            i += 5
            packet["value"] = binary_to_int(value_bits)

        else:  # operator packet
            length_type = bits[i+6]
            i += 7
            if length_type == '0':
                subpacket_index_limit = i + 15 + binary_to_int(bits[i:i+15])
                i += 15
                packet["subpacket_index_limit"] = subpacket_index_limit
            else:
                n_subpackets = binary_to_int(bits[i:i+11])
                i += 11
                packet["n_subpackets"] = n_subpackets
            packet["operator_id"] = operator_id
            operator_id += 1

        packets.append(packet)

    # Now fill in parent operator_ids
    parent_operators = []
    for packet in packets:
        while parent_operators and "subpacket_index_limit" in parent_operators[-1]:
            if parent_operators[-1]["subpacket_index_limit"] <= packet["starting_index"]:
                parent_operators.pop(-1)
            else:
                break
        if not parent_operators:
            packet["parent_operator_id"] = None
        else:
            packet["parent_operator_id"] = parent_operators[-1]["operator_id"]
            if "n_subpackets" in parent_operators[-1]:
                parent_operators[-1]["n_subpackets"] -= 1
                if not parent_operators[-1]["n_subpackets"]:
                    parent_operators.pop(-1)
        if packet["packet_type"] != 4:
            parent_operators.append(packet)

    # remove unneeded data
    for packet in packets:
        packet.pop("subpacket_index_limit", "")
        packet.pop("n_subpackets", "")

    # finally evaluate operator values, starting from the back
    evaluate_operator_values(packets)

    return packets


def task_1(packet_info):
    return sum([p["version"] for p in packet_info])


def task_2(packet_info):
    outer_operators = list(filter(lambda x: x["parent_operator_id"] is None, packet_info))
    assert len(outer_operators) == 1
    return outer_operators[0]["value"]


def main():
    data = ''
    for line in open(os.getcwd() + '/data/day_16.txt'):
        data = line.replace('\n', '')
    packet_info = scan_hexadecimal(data)
    pprint(packet_info)
    print(task_1(packet_info))
    print(task_2(packet_info))


if __name__ == '__main__':
    main()
