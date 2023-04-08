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
n = int(cmdlinearg('n')) # number of nodes
k = int(cmdlinearg('k')) # maximum number of nodes with A_i > 0
maxa = int(cmdlinearg('maxa')) # maximum value of A_i and B_i
mode = cmdlinearg('mode') # type of tree to generate

# Place a portion of the nodes based on the current mode
edges = []
if mode == "long" and n > 2:
    # Line mode, start with a long line
    for i in range(1, n // 2):
        edges += [(i, i - 1)]
elif mode == "star" and n > 3:
    # Star mode, place a few nodes with very high degree
    edges = [(0, 1)]
    for i in range(2, n // 2):
        edges += [(i, random.randint(0, 1))]
else:
    # Ranom mode, no predetermined edges
    pass

# Place random edges until there are enough
while len(edges) < n - 1:
    edges += [(len(edges) + 1, random.randint(0, len(edges)))]

# Shuffle the indices of the nodes
mapping = list(range(n))
random.shuffle(mapping)
edges = [(mapping[a], mapping[b]) for a, b in edges]
random.shuffle(edges)

# Get the neighbors of each node, for validation
neighbors = [[] for _ in range(n)]
for p, q in edges:
    neighbors[p] += [q]
    neighbors[q] += [p]

# Generate random constants until the solution is unique
while True:
    a_values = [random.randint(0, maxa) if i < k else 0 for i in range(n)]
    random.shuffle(a_values)

    b_values = [random.randint(1, maxa) for _ in range(n)]

    cache = {}
    def volume_of_branch(node, from_node=-1, current_distance=0):
        key = (node, from_node, current_distance)
        if key in cache: return cache[key]

        if current_distance ** 2 > maxa: return 0

        if from_node != -1:
            return volume_of_branch(node, -1, current_distance) - \
                volume_of_branch(from_node, node, current_distance + 1)

        total = a_values[node] // (b_values[node] + current_distance**2)

        for other in neighbors[node]:
            total += volume_of_branch(other, node, current_distance + 1)

        cache[key] = total
        return total

    possible = sorted(volume_of_branch(i) for i in range(n))

    # Ensure the solution is unique
    if possible[-1] != possible[-2]:
        break

print(n)
for a, b in zip(a_values, b_values):
    print(a, b)
for p, q in edges:
    print(p, q)
