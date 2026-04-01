import sys
from collections import deque

def solve():
    input_data = sys.stdin.readline().split()
    if not input_data: return
    r, c = map(int, input_data)
    
    board = [list(sys.stdin.readline().strip()) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]

    total_sheep = 0
    total_wolf = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(r):
        for j in range(c):
            if board[i][j] != '#' and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                
                area_sheep = 0
                area_wolf = 0
                
                while queue:
                    y, x = queue.popleft()

                    if board[y][x] == 'o':
                        area_sheep += 1
                    elif board[y][x] == 'v':
                        area_wolf += 1
                    
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]

                        if 0 <= ny < r and 0 <= nx < c:
                            if board[ny][nx] != '#' and not visited[ny][nx]:
                                visited[ny][nx] = True
                                queue.append((ny, nx))

                if area_sheep > area_wolf:
                    total_sheep += area_sheep
                else:
                    total_wolf += area_wolf

    print(total_sheep, total_wolf)

if __name__ == "__main__":
    solve()