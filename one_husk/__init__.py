import struct

def p64(x):
    return struct.pack('<Q', x)

def u64(x):
    return struct.unpack('<Q', x)[0]

def p32(x):
    return struct.pack('<I', x)

def p16(x):
    return struct.pack('<H', x)

class fakeFile(object):
    # Most variable names are inherited from
    # https://github.com/Gallopsled/pwntools/blob/cc6d272760/pwnlib/filepointer.py#L94-L338

    vars_ = {}
    fields = ['flags', '_IO_read_ptr', '_IO_read_end', '_IO_read_base', '_IO_write_base', '_IO_write_ptr', '_IO_write_end', '_IO_buf_base', '_IO_buf_end', '_IO_save_base', '_IO_backup_base', '_IO_save_end', 'markers', 'chain', 'fileno', '_flags2', '_old_offset', '_cur_column', '_vtable_offset', '_shortbuf', 'unknown1', '_lock', '_offset', '_codecvt', '_wide_data', 'unknown2', 'vtable', '_allocate_buffer', '_free_buffer']

    def __init__(self):
        self.setdefault()

    def setdefault(self):
        for field in self.fields:
            self.vars_[field] = 0

    def build(self):
        to_concat = []
        for field in self.fields:
            # Use 'and' for better performance
            if field != '_cur_column' and field != '_vtable_offset' and field != '_shortbuf':
                to_concat.append(p64(self.vars_[field]))
            else:
                if field == '_cur_column':
                    # short
                    to_concat.append(p32(self.vars_[field]))
                else:
                    # char
                    to_concat.append(p16(self.vars_[field]))

        return ''.join(to_concat)
