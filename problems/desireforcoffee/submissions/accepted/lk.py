#!/usr/bin/python3
n = int(input())
l = []
for _ in range(n):
    C,W,L = map(int,input().split())
    l.append((C,W,L))
l = sorted(l, key=lambda x : -(x[0] + x[1]))
d = [-1]*501
for t in l:
    for i in range(t[1],501):
        #obs care C=500 edge case
        if d[i] != -1:
            nw = min(i-t[1],t[0])
            d[nw] = mx = max(d[nw],d[i] + t[2])
        if i == 500:
          d[t[0]] =mx= max(d[t[0]],t[2])  
        
print(max(d))