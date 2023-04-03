from functools import cache

@cache
def volume_of_branch(node, from_node=-1, current_distance=0):
    if current_distance ** 2 > maximum_a:
        return 0

    if from_node != -1:
        return volume_of_branch(node, -1, current_distance) - \
            volume_of_branch(from_node, node, current_distance + 1)


    a, b = constants[node]
    total = a // (b + current_distance**2)

    for other in neighbors[node]:
        total += volume_of_branch(other, node, current_distance + 1)

    return total

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

print(max(range(n), key=lambda i: volume_of_branch(i)))
