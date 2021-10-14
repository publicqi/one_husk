# Not finished and possibly won't be finished. I've passed my age for IO_FILE exploits

# one_husk
This tool is an improved version of `pwnlib.filepointer` from pwntools. Most code are from [pwntools/filepointer.py](https://github.com/Gallopsled/pwntools/blob/cc6d272760/pwnlib/filepointer.py#L94-L338). In this improved tool, you can directly modify `struct _IO_str_fields _s` use this tool. You can also auto-generate a getshell payload.

 I name this module one_husk since house_of_husk is a great example that summarized this type of attack(change `global_max_fast`; fake a struct on the heap; overwrite `_IO_list_all`; ). 

## Installation

## Usage

## Test cases

## Technical stuff

The [class](https://docs.pwntools.com/en/stable/filepointer.html) from pwntools was way too old for modern exploits. Currently, as far as I am aware, there're two functions can be used to getshell: `_IO_str_overflow` and `_IO_str_finish`. The two functions will cast a file pointer to `_IO_strfile` and call methods inside them.

```c
void _IO_str_finish (_IO_FILE *fp, int dummy){
  if (fp->_IO_buf_base && !(fp->_flags & _IO_USER_BUF))
    (((_IO_strfile *) fp)->_s._free_buffer) (fp->_IO_buf_base);
  ...
}

int _IO_str_overflow (_IO_FILE *fp, int c){
...
	  new_buf
	    = (char *) (*((_IO_strfile *) fp)->_s._allocate_buffer) (new_size);
...}
```

So, class from pwntools is limited to `IO_FILE` only therefore **not elegant** enough to write something like

```python
fake_file._allocate_buffer = p64(libc_base + libc.symbols["system"])
```

Another thing is that under many circumstances, building such a struct is just **repetitive work**. For example, if you want to use `_IO_str_finish` to getshell, all you need to bypass is `_IO_write_ptr >_IO_write_base`. And you need to set `_IO_buf_base` to be `addr_of_bin_sh` and `fp->_s._free_buffer` to be `addr_of_system`.