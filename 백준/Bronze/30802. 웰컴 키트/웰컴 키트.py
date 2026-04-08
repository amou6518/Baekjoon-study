import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

total_t_bundles = 0
for count in sizes:
    if count == 0:
        continue
    total_t_bundles += (count // t)
    if count % t > 0:
        total_t_bundles += 1

p_bundles = n // p
p_singles = n % p
print(total_t_bundles)
print(p_bundles, p_singles)