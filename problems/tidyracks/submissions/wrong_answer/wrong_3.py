from collections import defaultdict

def main():
    n, k = map(int, input().split())

    racks = []
    for _ in range(n):
        racks += [[int(w) for w in input().split()][1:]]

    empty = n * k - sum(len(rack) for rack in racks)

    if empty >= k:
        count_per_type = defaultdict(lambda: 0)
        for rack in racks:
            for weight in rack:
                count_per_type[weight] += 1

        needed_racks = sum((count + k - 1) // k for count in count_per_type.values())
        return needed_racks <= len(racks)

    locked = k - empty
    for rack in racks:
        first = rack[0]
        if any(w != first for w in rack[:locked]):
            return False

    # Whoops, here we forgot to test if the weights can be distributed among the racks
    return True

if main():
    print("Yes")
else:
    print("No")
