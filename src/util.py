def read_varlen(data):
    next_byte = True
    value = 0
    for char in data:
        # is the hi-bit set?
        if not (char & 0x80):
            # no next BYTE
            next_byte = False
        # mask out the 8th bit
        char = char & 0x7F
        # shift last value up 7 bits
        value = value << 7
        # add new value
        value += char
        if not next_byte:
            break
    return value


def write_varlen(value):
    res = []
    chr1 = (value & 0x7F)
    value >>= 7
    if value:
        chr2 = ((value & 0x7F) | 0x80)
        value >>= 7
        if value:
            chr3 = ((value & 0x7F) | 0x80)
            value >>= 7
            if value:
                chr4 = ((value & 0x7F) | 0x80)
                res = [chr4, chr3, chr2, chr1]
            else:
                res = [chr3, chr2, chr1]
        else:
            res = [chr2, chr1]
    else:
        res = [chr1]
    return bytes(res)
