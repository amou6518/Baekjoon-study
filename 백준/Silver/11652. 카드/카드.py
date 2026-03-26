import sys
n = int(sys.stdin.readline())
cards = {}

for i in range(n):
    x = int(sys.stdin.readline())
    if x in cards:
        cards[x] += 1
    else:
        cards[x] = 1

result = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])