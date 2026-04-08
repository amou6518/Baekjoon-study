import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
my_cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

count_map = Counter(my_cards)
result = []
for target in targets:
    result.append(str(count_map[target]))

print(" ".join(result))