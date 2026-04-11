import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
 
    count = 0 
    
    while queue:
        current = queue.popleft()

        if any(current[0] < doc[0] for doc in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == m:
                print(count)
                break