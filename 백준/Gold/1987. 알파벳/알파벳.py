import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().strip())) for _ in range(r)]

def solve():
    q = set([(0, 0, (board[0][0],))])
    max_count = 0

    while q:
        x, y, path = q.pop()
        max_count = max(max_count, len(path))

        if max_count == 26:
            return 26

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c:
                char_val = board[nx][ny]
                if char_val not in path:
                    q.add((nx, ny, path + (char_val,)))
    
    return max_count

print(solve())