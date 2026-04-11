import sys

m, n = map(int, sys.stdin.readline().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        is_prime[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))

for i in range(m, n + 1):
    if is_prime[i]:
        print(i)