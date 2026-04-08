import sys
from collections import deque

def elv():
    f, s, g, u, d = map(int, sys.stdin.readline().split())

    visited = [-1] * (f + 1)
    
    queue = deque([s])
    visited[s] = 0 
    
    while queue:
        curr = queue.popleft()
        
        if curr == g:
            print(visited[curr])
            return

        for next_floor in (curr + u, curr - d):
            if 1 <= next_floor <= f and visited[next_floor] == -1:
                visited[next_floor] = visited[curr] + 1
                queue.append(next_floor)
    print("use the stairs")

elv()