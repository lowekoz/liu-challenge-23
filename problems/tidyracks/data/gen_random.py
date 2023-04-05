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
n = int(cmdlinearg('n')) # number of racks upper limit
k = int(cmdlinearg('k')) # stack size upper limit
mode = cmdlinearg('mode',default="") # empty, no_empty : x <= (n-1)k, x > (n-1)k 
maxa = cmdlinearg('maxa',default="")

#flag = int(cmdlinearg('flag',0))

N = random.randint(1,n)
K = random.randint(1,k)

if maxa != "":
    N = n
    K = k 

x = random.randint(0,(N-1)*K) # max total number of weights if mode "empty"
rm = random.randint(0,K-1) # remove at most rm number of weights for a total of >= NK - rm weights, rm < K

# output
print(N,K) 
Ws = [5,10,15,20]
for _ in range(N):
    Bi = random.randint(0,K)
    if mode == "empty":
        Bi = random.randint(0,min(x,K))
        x -= Bi
    elif mode == "no_empty":
        Bi = K
        allowance = random.randint(0,rm)
        Bi -= allowance
        rm -= allowance

    line = [Bi]
    for j in range(Bi):
        line.append(Ws[random.randint(0, 3)])
    print(*line)
