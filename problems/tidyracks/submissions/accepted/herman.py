#!/usr/bin/python3
from collections import defaultdict

def main():
    n, k = map(int, input().split())

    racks = []
    for _ in range(n):
        racks += [[int(w) for w in input().split()][1:]]

    empty = n * k - sum(len(rack) for rack in racks)

    # If a single rack is completely empty, all weights can be moved freely.
    if empty >= k:
        count_per_type = defaultdict(lambda: 0)
        for rack in racks:
            for weight in rack:
                count_per_type[weight] += 1

        needed_racks = sum((count + k - 1) // k for count in count_per_type.values())
        return needed_racks <= len(racks)

    # Otherwise, the bottom weights cannot be moved. Make sure they are sorted.
    locked = k - empty
    for rack in racks:
        first = rack[0]
        if any(w != first for w in rack[:locked]):
            return False
    
    # Count the amount of racks to be used for each type.
    racks_per_type = defaultdict(lambda: 0)
    for rack in racks:
        racks_per_type[rack[0]] += 1

    count_per_type = defaultdict(lambda: 0)
    for rack in racks:
        for weight in rack:
            count_per_type[weight] += 1

    # Test if it is enough
    return all(count_per_type[weight] <= racks_per_type[weight] * k for weight in count_per_type)

if main():
    print("Yes")
else:
    print("No")
