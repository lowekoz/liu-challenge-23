#!/usr/bin/python3

import sys

lines = sys.stdin.readlines()
correct_inp = []

#windows newline
for i in range(len(lines)):
    lines[i] = lines[i].replace('\r',"")

n = int(lines[0])
assert(n >= 1)
assert(n <= 100000)

correct_inp.append("%d\n" % n)

a = list(lines[1].split())
for el in a:
    assert(abs(int(el)) <= 1000)

correct_inp.append(" ".join(a) + '\n')
assert "".join(correct_inp) == "".join(lines)

exit(42)