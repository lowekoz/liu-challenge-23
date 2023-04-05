import sys
import random
import string

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default


def randstr(len):
    letters = string.ascii_uppercase
    extra_letters = " .!?"
    msg = ''.join(random.choice(letters) if random.random() > extra else random.choice(extra_letters) for _ in range(len))
    return msg


def generate_answer(msg, step):
    res = "".join([chr((ord(c)-ord("A")+step)%26+ord("A")) if ord("A") <= ord(c) <= ord("Z") else c for c in msg])
    return res


random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n')) # number of test cases upper limit
m = int(cmdlinearg('m')) # message length upper limit
extra = float(cmdlinearg('extra',default="0.1")) # ratio of extra characters ( .!?)

N = random.randint(1,n)
M = random.randint(1,m)

# Output
print(N)
for _ in range(N):
    S = random.randint(0, 25)
    print(S)
    L = random.randint(1, M)
    msg = randstr(L)
    print(msg)
