import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
prime_count = 0

for num in numbers:
    if num < 2:
        continue   
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False 
            break
    if is_prime:
        prime_count += 1
print(prime_count)