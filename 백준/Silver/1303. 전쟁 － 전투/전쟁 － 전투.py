import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(m)]

    visited = [[False] * n for _ in range(m)]
    

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    white_power = 0
    blue_power = 0 

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                color = grid[i][j]
                queue = deque([(i, j)])
                visited[i][j] = True
                count = 1 

                while queue:
                    y, x = queue.popleft()
                    
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
  
                        if 0 <= ny < m and 0 <= nx < n:

                            if not visited[ny][nx] and grid[ny][nx] == color:
                                visited[ny][nx] = True
                                count += 1
                                queue.append((ny, nx))

                if color == 'W':
                    white_power += (count ** 2)
                else:
                    blue_power += (count ** 2)

    print(white_power, blue_power)

if __name__ == "__main__":
    solve()