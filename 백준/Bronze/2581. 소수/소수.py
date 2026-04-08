M = int(input())
N = int(input())

primes = []

for i in range(M, N + 1):
    if i < 2: 
        continue
    for j in range(2, i):
        if i % j == 0:
            break  
    else:
        primes.append(i)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))