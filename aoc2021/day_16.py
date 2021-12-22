import os


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


def scan_hexadecimal(hexadecimal):
    """
    Returns a list of dicts containing packet information
    {
        "version": <int>
        "packet_type": <int>
        "value": Optional[int] (None if not literal_value)
        # "operator_id": Optional[int] (id of operator containing packet)
        # "operator_position
    }
    """
    bits = convert_hexadecimal_to_bits(hexadecimal)
    packets = []
    i = 0

    while i < len(bits.strip('0')):  # i should be the first index of a new packet
        version = binary_to_int(bits[i: i+3])
        packet_type = binary_to_int(bits[i+3:i+6])

        if packet_type == 4:  # literal value
            value_bits = ''
            i += 6
            while bits[i] == '1':
                value_bits += bits[i+1: i+5]
                i += 5
            value_bits += bits[i+1: i+5]  # get final one
            i += 5
            packets.append({
                "version": version,
                "packet_type": packet_type,
                "value": binary_to_int(value_bits),
            })

        else:  # operator packet
            length_type = bits[i+6]
            i += 7
            if length_type == '0':
                sub_packet_length = binary_to_int(bits[i:i+15])
                i += 15
            else:
                n_sub_packets = binary_to_int(bits[i:i+11])
                i += 11
            packets.append({
                "version": version,
                "packet_type": packet_type,
                "value": None,
            })

    return packets


def task_1(packet_info):
    return sum([p["version"] for p in packet_info])



def main():
    data = ''
    for line in open(os.getcwd() + '/data/day_16.txt'):
        data = line.replace('\n', '')
    packet_info = scan_hexadecimal(data)
    from pprint import pprint
    pprint(packet_info)
    print(task_1(packet_info))
    # print(task_2(data))


if __name__ == '__main__':
    main()
