import sys
from collections import deque

def solve():
    m, n, k = map(int, sys.stdin.readline().split())

    grid = [[0] * n for _ in range(m)]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    areas = [] 

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1 
                queue = deque([(i, j)])
                width = 1
                
                while queue:
                    y, x = queue.popleft()
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        
                        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == 0:
                            grid[ny][nx] = 1
                            width += 1
                            queue.append((ny, nx))
                
                areas.append(width)

    print(len(areas))
    print(*(sorted(areas))) 

if __name__ == "__main__":
    solve()