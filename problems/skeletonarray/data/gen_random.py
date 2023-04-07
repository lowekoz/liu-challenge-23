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
maxa = cmdlinearg('maxa',default="")

N = random.randint(1,n)
if maxa != "":
    N = n

A = []
for _ in range(N):
    A.append(random.randint(-m, m))

print(N)
print(*A)
