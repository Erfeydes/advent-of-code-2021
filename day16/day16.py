from math import prod

filename = "input.txt"
bits = "".join(map("{:08b}".format, bytes.fromhex(open(filename).read())))


class BitDecoder:
    def __init__(self):
        self.position = 0

    def decode_int(self, nbits):
        res = int(bits[self.position:self.position + nbits], 2)
        self.position += nbits
        return res

    def decode_packets(self, nbits):
        end = self.position + nbits
        packets = []
        while self.position < end:
            packets.append(self.decode_packet())
        return packets

    def decode_data(self, tid):
        if tid == 4:
            value = 0
            group = 0b10000
            while group & 0b10000:
                group = self.decode_int(5)
                value = (value << 4) + (group & 0b1111)
            return value
        if self.decode_int(1):
            return [self.decode_packet() for _ in range(self.decode_int(11))]
        return self.decode_packets(self.decode_int(15))

    def decode_packet(self):
        version = self.decode_int(3)
        type_id = self.decode_int(3)
        data = self.decode_data(type_id)
        return version, type_id, data


def sum_versions(p):
    version, type_id, data = p
    return version if type_id == 4 else version + sum(map(sum_versions, data))


def evaluate_packet(p):
    _, type_id, data = p
    if type_id == 4:
        return data

    values = map(evaluate_packet, data)

    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        return prod(values)
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)

    a, b = values

    if type_id == 5:
        return int(a > b)
    elif type_id == 6:
        return int(a < b)
    elif type_id == 7:
        return int(a == b)


decoder = BitDecoder()
packet = decoder.decode_packet()

print("Part 1 solution:", sum_versions(packet), "Part 2 solution:", evaluate_packet(packet))
