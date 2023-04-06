#!/usr/bin/python3

U = set()
for i in range(ord('A'),ord('Z')+1):
    U.add(chr(i))

U.add('!')
U.add('?')
U.add('.')
U.add(' ')

N = int(input())
assert 0 < N <= 100

for _ in range(N):
    S = int(input())
    assert 0 <= S <= 25

    msg = input()
    assert 0 < len(msg) <= 1e3

    for ch in msg:
        assert((ch in U))

exit(42)