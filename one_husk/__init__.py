import struct


def p64(x):
    return struct.pack('<Q', x)


def u64(x):
    return struct.unpack('<Q', x)[0]


class fakeFile(object):
    # Most variable names are inherited from
    # https://github.com/Gallopsled/pwntools/blob/cc6d272760/pwnlib/filepointer.py#L94-L338

    vars_ = []
    length = {}

    def __init__(self):
        pass
