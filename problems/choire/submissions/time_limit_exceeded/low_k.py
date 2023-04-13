#!/usr/bin/env python3

import sys

sys.setrecursionlimit(30000)

def propagate_volume(node, a, b, from_node=-1, current_distance=0):
    volumes[node] += a // (b + current_distance ** 2)

    for other in neighbors[node]:
        if other != from_node:
            propagate_volume(other, a, b, node, current_distance + 1)

n = int(input())

constants = []
for _ in range(n):
    a, b = input().split()
    constants += [(int(a), int(b))]

maximum_a = max(a for a, b in constants)

neighbors = [[] for _ in range(n)]

for _ in range(n - 1):
    p, q = input().split()
    p, q = int(p), int(q)
    neighbors[p] += [q]
    neighbors[q] += [p]

volumes = [0] * n
for node, (a, b) in enumerate(constants):
    if a:
        propagate_volume(node, a, b)

print(max(range(n), key=lambda i: volumes[i]))
