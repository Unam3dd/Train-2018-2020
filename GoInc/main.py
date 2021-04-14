from ctypes import *

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

if __name__ == "__main__":
    lib = cdll.LoadLibrary("./awesome.lib")
    lib.PopShell()
    print(lib.Add(1,2))
    msg = GoString(b"Hello",6)
    lib.Say(msg)