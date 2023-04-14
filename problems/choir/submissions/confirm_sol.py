#!/usr/bin/env python3

N = int(input())

A = []
B = []

neighbors = [set() for _ in range(N)]

for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

for j in range(N-1):
    pj, qj = map(int, input().split())
    neighbors[pj].add(qj)
    neighbors[qj].add(pj)

def volume_at(node, exclude, dist):
    volume = int(A[node] / (B[node] + dist**2))
    for n in neighbors[node]:
        if n != exclude:
            volume += volume_at(n, node, dist+1)
    return volume

max_volume = -1
idx = -1
for x in range(N):
    volume = volume_at(x, -1, 0)
    if volume > max_volume:
        max_volume = volume
        idx = x

print(idx)