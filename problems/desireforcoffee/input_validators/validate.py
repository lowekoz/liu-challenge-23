#!/usr/bin/python3
import sys

lines = sys.stdin.readlines()
correct_inp = []

#windows newline
for i in range(len(lines)):
    lines[i] = lines[i].replace('\r',"")


n = int(lines[0])
assert n <= 1000 and n >= 1
assert lines[0] == f"{n}\n"

correct_inp.append("%d\n" % n)


for line in lines[1:n+1]:
    c,w,l = map(int,line.split())
    assert c >= 1 and w >= 1 and l >= 1
    assert c <= 500 and w <= 500 and l <= 500
    assert line == f"{c} {w} {l}\n"
    correct_inp.append("%d %d %d\n" % (c,w,l))

assert "".join(correct_inp) == "".join(lines)

exit(42)