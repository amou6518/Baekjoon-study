import sys
from collections import deque

def rain():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    board = []
    max_height = 0
    
    idx = 1
    for _ in range(n):
        row = list(map(int, input_data[idx:idx+n]))
        board.append(row)
        max_height = max(max_height, max(row))
        idx += n

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ans = 1 

    def bfs(x, y, h, visited):
        q = deque([(x, y)])
        visited[x][y] = True
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and board[nx][ny] > h:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    for h in range(1, max_height):
        visited = [[False] * n for _ in range(n)]
        count = 0
        
        for i in range(n):
            for j in range(n):
                if board[i][j] > h and not visited[i][j]:
                    bfs(i, j, h, visited)
                    count += 1
        
        ans = max(ans, count)

    print(ans)

rain()