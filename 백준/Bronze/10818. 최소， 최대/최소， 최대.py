import sys

n= int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

max_value = max(numbers)
min_value = min(numbers)

print(min_value, max_value)