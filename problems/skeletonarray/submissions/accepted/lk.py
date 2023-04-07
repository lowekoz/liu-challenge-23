#!/usr/bin/python3
from math import ceil,floor
n = int(input())
a = list(map(int,input().split()))

# b = [e e-a[0] e-a[0]-a[1] ...] for some e
aneg = [0]*(n+1) # 0 -a[0] -a[0]-a[1] ...
for i in range(n):
    aneg[i+1] = aneg[i] - a[i]


# sum(b) = e*(n+1) + sum(aneg), chose e so that abs(sum(b)) is minimum
sm = sum(aneg)
# want sum(b) = 0
# candidates (safety)
e = (-sm)//(n+1)
eup =  e+1
edw = e-1

best = e
if abs(eup*(n+1) + sm) <= abs(best*(n+1)+sm): # max ans condition, eup > e > edw always
    best = eup
if abs(edw*(n+1) + sm) < abs(best*(n+1)+sm):
    best = edw

out = [0]*(n+1)
for i in range(n+1):
    out[i] = best + aneg[i]
print(*out)

'''
1
3

ans both
2 -1
1 -2
'''
