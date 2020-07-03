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
        self.setdefault()

    def setdefault(self):
        self.flags = 0
        self._IO_read_ptr = 0
        self._IO_read_end = 0
        self._IO_read_base = 0
        self._IO_write_base = 0
        self._IO_write_ptr = 0
        self._IO_write_end = 0
        self._IO_buf_base = 0
        self._IO_buf_end = 0
        self._IO_save_base = 0
        self._IO_backup_base = 0
        self._IO_save_end = 0
        self.markers = 0
        self.chain = 0
        self.fileno = 0
        self._flags2 = 0
        self._old_offset = 0
        self._cur_column = 0
        self._vtable_offset = 0
        self._shortbuf = 0
        self.unknown1 = 0
        self._lock = 0
        self._offset = 0
        self._codecvt = 0
        self._wide_data = 0
        self.unknown2 = 0
        self.vtable = 0

        self._allocate_buffer = 0
        self._free_buffer = 0
