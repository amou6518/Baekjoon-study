from collections import deque

n, k = map(int, input().split())
MAX = 100001
dist = [-1] * MAX

def bfs():
    q = deque([n])
    dist[n] = 0 
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(dist[x])
            return

        if 0 <= 2 * x < MAX and dist[2 * x] == -1:
            dist[2 * x] = dist[x]
            q.appendleft(2 * x)
            
        for nx in (x - 1, x + 1):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()