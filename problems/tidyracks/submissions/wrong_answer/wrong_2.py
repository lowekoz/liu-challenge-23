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

    # Whoops, here we forgot to check if the locked part is sorted

    racks_per_type = defaultdict(lambda: 0)
    for rack in racks:
        racks_per_type[rack[0]] += 1

    count_per_type = defaultdict(lambda: 0)
    for rack in racks:
        for weight in rack:
            count_per_type[weight] += 1

    return all(count_per_type[weight] <= racks_per_type[weight] * k for weight in count_per_type)

if main():
    print("Yes")
else:
    print("No")
