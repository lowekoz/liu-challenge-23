#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

n = int(lines[0])
assert lines[0].strip() == f"{n}"

for line in lines[1:n+1]:
    a, b = map(int, line.split())
    assert a >= 0 and b > 0
    assert line.strip() == f"{a} {b}"
    assert a <= 50 and b <= 50

data = list(range(n))

def union_find(i):
    global data
    visited = []
    while data[i] != i:
        visited += [i]
        i = data[i]
    for v in visited:
        data[v] = i
    return i

for line in lines[n+1:]:
    p, q = map(int, line.split())
    assert 0 <= p < n and 0 <= q < n 
    assert line.strip() == f"{p} {q}"

    p = union_find(p)
    q = union_find(q)
    assert p != q, "cycles in graph"
    data[p] = data[q]

assert len(set(union_find(i) for i in range(n))) == 1, "graph not connected"

exit(42)