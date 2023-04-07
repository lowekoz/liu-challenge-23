#!/usr/bin/python3
n = int(input())
assert(n >= 1)
assert(n <= 100000)
a = list(map(int,input().split()))
for el in a:
    assert(abs(el) <= 1000)
exit(42)