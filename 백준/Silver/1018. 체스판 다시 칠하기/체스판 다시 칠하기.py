import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

min_repaint = float('inf')

for i in range(n - 7):
    for j in range(m - 7): 
        
        white_start = 0 
        black_start = 0 
        
        for r in range(i, i + 8):
            for c in range(j, j + 8):
              
                if (r + c) % 2 == 0:
                    if board[r][c] != 'W': white_start += 1
                    if board[r][c] != 'B': black_start += 1
                else:
                    if board[r][c] != 'B': white_start += 1
                    if board[r][c] != 'W': black_start += 1
        

        min_repaint = min(min_repaint, white_start, black_start)

print(min_repaint)