import sys
from collections import deque

def solve():
    line = sys.stdin.readline().split()
    if not line: return
    n, m, k = map(int, line)
    
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        r, c = map(int, sys.stdin.readline().split())
        grid[r][c] = 1 
    
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    max_waste_size = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if grid[i][j] == 1 and not visited[i][j]:

                queue = deque([(i, j)])
                visited[i][j] = True
                current_waste_size = 1 
                
                while queue:
                    cr, cc = queue.popleft()
                    
                    for d in range(4):
                        nr, nc = cr + dr[d], cc + dc[d]
                        
               
                        if 1 <= nr <= n and 1 <= nc <= m:
                            if grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                current_waste_size += 1
                                queue.append((nr, nc))
                

                max_waste_size = max(max_waste_size, current_waste_size)

    print(max_waste_size)

if __name__ == "__main__":
    solve()