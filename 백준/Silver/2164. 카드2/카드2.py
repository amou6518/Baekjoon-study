import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()

    if cards:
        moved_card = cards.popleft()
        cards.append(moved_card)

print(cards[0])