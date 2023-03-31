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



random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n')) # array size
m = int(cmdlinearg('m')) # magnitude numbers

N = random.randint(2,n)
A = []
for _ in range(N):
    A.append((random.randint(0, m), random.randint(0, m), random.randint(0, m)))

print(N)
for tup in A:
    print(tup[0], tup[1], tup[2])
