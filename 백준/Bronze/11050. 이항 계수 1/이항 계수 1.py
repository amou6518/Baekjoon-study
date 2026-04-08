import sys

n, k = map(int, sys.stdin.readline().split())

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

if k < 0 or k > n:
    print(0)
else:
    ans = factorial(n) // (factorial(k) * factorial(n - k))
    print(ans)