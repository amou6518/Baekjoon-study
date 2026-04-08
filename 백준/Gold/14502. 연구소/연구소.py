import sys

input = sys.stdin.read
def virus():
    data = input().split()
    n, m = int(data[0]), int(data[1])
    board = []
    index = 2
    for i in range(n):
        board.append(list(map(int, data[index:index+m])))
        index += m

    empty = []
    virus = []
    for r in range(n):
        for c in range(m):
            if board[r][c] == 0: empty.append((r, c))
            elif board[r][c] == 2: virus.append((r, c))

    max_safe = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def get_score():
        visited = [[False] * m for _ in range(n)]
        q = virus[:] # 바이러스 초기 위치 복사
        
        infected_count = 0
        queue = virus[:]
        
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if board[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        infected_count += 1
                        queue.append((nr, nc))

        return len(empty) - 3 - infected_count

    def backtracking(start, count):
        nonlocal max_safe
        if count == 3:
            max_safe = max(max_safe, get_score())
            return

        for i in range(start, len(empty)):
            r, c = empty[i]
            board[r][c] = 1 
            backtracking(i + 1, count + 1)
            board[r][c] = 0 

    backtracking(0, 0)
    print(max_safe)

virus()