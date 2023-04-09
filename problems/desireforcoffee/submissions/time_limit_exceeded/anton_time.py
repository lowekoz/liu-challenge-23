import sys

sys.setrecursionlimit(15000)
def max_stack(capacity, current_turtle):
    global turtles
    
    if current_turtle == len(turtles):
        return 0

    dist1 = 0

    if capacity - turtles[current_turtle][1] >= 0:  
        local_capacity = min(capacity-turtles[current_turtle][1], turtles[current_turtle][0])
        dist1 = turtles[current_turtle][2] + max_stack(local_capacity, current_turtle+1)

    dist2 = max_stack(capacity, current_turtle+1)

    return max(dist1, dist2)


n = int(input())
turtles = []
for i in range(n):
    c, w, l = map(int, input().split())
    turtles.append((c, w, l))


turtles = sorted(turtles, key=lambda x: x[0]+x[1], reverse=True) #sort by sum of capacity and weight
print(max_stack(float('inf'), 0))