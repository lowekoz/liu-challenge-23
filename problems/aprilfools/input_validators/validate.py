
N = int(input())
assert 0 < N <= 100

for _ in range(N):
    S = int(input())
    assert 0 <= S <= 25

    msg = input()
    assert 0 < len(msg) <= 1e3
