import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
m = max(scores)
total_sum = sum(scores)

new_average = (total_sum * 100) / (m * n)
print(new_average)