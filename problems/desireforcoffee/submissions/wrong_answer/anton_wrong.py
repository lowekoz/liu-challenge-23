import sys
from collections import defaultdict

def def_value():
    return -1

dp = defaultdict(def_value)

sys.setrecursionlimit(15000)
def max_stack(capacity, current_turtle):
    global turtles
    global dp
    
    if current_turtle == len(turtles):
        return 0
    dist1 = 0

    if capacity - turtles[current_turtle][1] >= 0:  
        local_capacity = min(capacity-turtles[current_turtle][1], turtles[current_turtle][0])
        if dp[(local_capacity, current_turtle+1)] != -1:
            sub_stack = dp[(local_capacity, current_turtle+1)]
        else:
            sub_stack = max_stack(local_capacity, current_turtle+1)
        dist1 = turtles[current_turtle][2] + sub_stack

    if dp[(capacity, current_turtle+1)] != -1:
        sub_stack = dp[(capacity, current_turtle+1)]
    else:
        sub_stack = max_stack(capacity, current_turtle+1)
    dist2 = sub_stack

    dp[(capacity, current_turtle)] = max(dist1, dist2)
    return max(dist1, dist2)


n = int(input())
turtles = []
for i in range(n):
    c, w, l = map(int, input().split())
    turtles.append((c, w, l))

turtles.sort(reverse=True)
print(max_stack(float('inf'), 0))