def main() -> None:
    with open('input.txt') as file:
        input_data = file.read()

    # input_data = '8A004A801A8002F478'

    binary_string = ""
    for char in input_data:
        as_str = bin(int(char, 16))[2:]
        as_str = as_str.rjust(4, "0")
        binary_string += as_str
    version = process_term(binary_string)
    print(version)


def process_term(term: str) -> int:
    version_sum = int(term[0:3], 2)
    type_id = int(term[3:6], 2)

    if type_id == 4:
        value = ''
        i = 6
        while term[i:].startswith('1'):
            value += term[i + 1:i + 5]
            i += 5
        value += term[i + 1:i + 5]
        i += 5
    else:
        length_type = term[6]
        if length_type == '0':
            length = int(term[7:22], 2)
            subpackets = term[22: 22 + length]
            subpacket_list = split_subpackets(subpackets)
            for subpacket in subpacket_list:
                version_sum += process_term(subpacket)
        if length_type == '1':
            packet_number = int(term[7:18], 2)
            subpackets = term[18:]
            subpacket_list = split_subpackets(subpackets, packet_number)
            for subpacket in subpacket_list:
                version_sum += process_term(subpacket)
    return version_sum


def split_subpackets(subpackets: str, packets: int = -1) -> list:
    subpacket_list = []

    if subpackets[3:6] == '100':
        i = 0
        packet = subpackets[0:6]
        bitgroup_start = 6
        index = bitgroup_start + i * 5
        while index < len(subpackets) and (packets < 0 or len(subpacket_list) < packets):
            packet += subpackets[index:index+5]
            if subpackets[index] == '0':
                subpacket_list.append(packet)
                packet = subpackets[index + 5:index + 11]
                bitgroup_start += 6

            i += 1
            index = bitgroup_start + i * 5
    else:
        while len(subpackets) > 6:
            if subpackets[6] == '0':
                length = int(subpackets[7:22], 2)
                subpacket_list.append(subpackets[0:22 + length])
                subpackets = subpackets[22 + length:]
            elif subpackets[6] == '1':
                subpacket_list.append(subpackets)
                subpackets = ''
        print('\n'.join(subpacket_list))
        print('--------------')

    return subpacket_list


if __name__ == '__main__':
    main()
