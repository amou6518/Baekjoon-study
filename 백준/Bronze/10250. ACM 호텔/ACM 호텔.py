import sys

a = int(sys.stdin.readline())
for _ in range(a):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    number = (n // h) + 1
    if floor == 0:
        floor = h
        number = n // h

    print(f"{floor}{number:02d}")