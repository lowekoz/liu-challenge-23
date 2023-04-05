#!/usr/bin/python3
ws = {5,10,15,20}

n,k = map(int,input().split())
assert(n > 0)
assert(n<=int(1e4))
assert(k >= 0)
assert(k <= 100)

for _ in range(n):
    lista = list(map(int,input().split()))
    assert(len(lista) > 0)
    bi = lista[0]
    assert(bi >= 0)
    assert(bi <= k)
    assert(len(lista) == bi+1)
    for j in range(bi):
        el = lista[j+1]
        assert(el in ws)

exit(42)
