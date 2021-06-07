from struct import unpack

B_SIZE = 8 + 2 + 16
C_SIZE = 4 + 4 + 2 * 3
D_SIZE = 4 * 3 + 4


def parse_a(offset, byte_string):
    a1_parsed = parse_b(offset, byte_string)

    a234567_bytes = byte_string[offset + B_SIZE:offset + B_SIZE + 31]
    a234567_parsed = unpack('QbBBBBBBfdI', a234567_bytes)

    return {
        'A1': a1_parsed,
        'A2': a234567_parsed[0],
        'A3': a234567_parsed[1],
        'A4': list(a234567_parsed[2:8]),
        'A5': a234567_parsed[8],
        'A6': a234567_parsed[9],
        'A7': parse_d(a234567_parsed[10], byte_string),
    }


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = unpack('dHIIII', b_bytes)

    b3 = [parse_c(b_parsed[2], byte_string), parse_c(b_parsed[3], byte_string),
          parse_c(b_parsed[4], byte_string), parse_c(b_parsed[5], byte_string)]

    return {
        'B1': b_parsed[0],
        'B2': b_parsed[1],
        'B3': b3,
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = unpack('IIhhh', c_bytes)
    c1_bytes = byte_string[c_parsed[1]:c_parsed[1] + c_parsed[0]]
    c1_parsed = unpack('h' * c_parsed[0], c1_bytes)

    return {
        'C1': c1_parsed,
        'C2': list(c_parsed[2:5]),
    }


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = unpack('iiii', d_bytes)

    return {
        'D1': list(d_parsed[0:3]),
        'D2': d_parsed[3],
    }


def f31(byte_string):
    return parse_a(4, byte_string)

print(f31((b'GRLX\xd2\xf1)\xf0\x89B\xe0?\xbchA\x00\x00\x00W\x00\x00\x00m\x00'
b'\x00\x00\x83\x00\x00\x00\xca\xb9\xd63\x0e\xe5+\xff\x03:\xdd:D\x7f.\x08\r\x91'
b'>\x88\xcbt\xd9\xa0\xeb\xca?\x91\x00\x00\x00\xfc\xcb\x82\x12\x02\x00\x00'
b'\x00=\x00\x00\x00~\xa5\x15\x86z\xd6\xd7\xcb\xf5L\xa35\x94g\x04\x00\x00\x00O'
b'\x00\x00\x00\x1bN\xf7\xb9$\x19\x8aq\x80\x1d\x80S\x82\xf3\x04\x00\x00'
b'\x00e\x00\x00\x00~\x0fe\x94\xbc\xa88\x86\x81\x13\x83\x84PC\x04\x00\x00\x00{'
b"\x00\x00\x00\xec\xbaK\xf8'\x12\xce|\x11\x8c\x02\x80`W\x84t\xc6o\xa5\xb2\xcd"
b'\xc1')))
