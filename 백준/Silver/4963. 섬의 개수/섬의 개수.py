import sys
from collections import deque

def solve():
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    def bfs(x, y, h, w, land):
        queue = deque([(x, y)])
        land[x][y] = 0 
        
        while queue:
            cx, cy = queue.popleft() 

            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1:
                    land[nx][ny] = 0 
                    queue.append((nx, ny)) 
    while True:
        # 입력 처리
        line = sys.stdin.readline().split()
        if not line: break
        
        w, h = map(int, line)
        if w == 0 and h == 0: break

        land = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        
        island_count = 0

        for i in range(h):
            for j in range(w):

                if land[i][j] == 1:
                    island_count += 1 
                    bfs(i, j, h, w, land)
                    
        print(island_count)

if __name__ == "__main__":
    solve()