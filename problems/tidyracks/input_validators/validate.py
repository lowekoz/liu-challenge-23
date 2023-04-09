#!/usr/bin/python3

import sys

lines = sys.stdin.readlines()
correct_inp = []

#windows newline
for i in range(len(lines)):
    lines[i] = lines[i].replace('\r',"")

ws = {5,10,15,20}

n,k = map(int,lines[0].split())
assert(n > 0)
assert(n<=int(1e4))
assert(k >= 0)
assert(k <= 100)

correct_inp.append("%d %d\n" % (n,k))

for i in range(n):
    lista = list(map(int,lines[i+1].split()))
    assert(len(lista) > 0)
    bi = lista[0]
    assert(bi >= 0)
    assert(bi <= k)
    assert(len(lista) == bi+1)
    for j in range(bi):
        el = lista[j+1]
        assert(el in ws)
    
    correct_inp.append(" ".join(map(str,lista)) + '\n')

assert "".join(correct_inp) == "".join(lines)

exit(42)
