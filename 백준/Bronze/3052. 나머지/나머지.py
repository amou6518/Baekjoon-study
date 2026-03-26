import sys
r = set()

for _ in range(10):
    num = int(sys.stdin.readline())
    r.add(num % 42)

print(len(r))