import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default



target = int(cmdlinearg('target'))


if target == 1:
    print(*[2,4])
    print(*[2,5,10])
    print(*[2,15,20])
elif target == 2:
    print(*[3,4])
    print(*[4,15,15,5,5])
    print(*[3,10,10,15])
    print(*[3,5,10,10])
elif target == 3:
    print(*[2,4])
    print(*[4,20,15,10,5])
    print(*[1,20])
else:
    assert(False,"faulty arg")
