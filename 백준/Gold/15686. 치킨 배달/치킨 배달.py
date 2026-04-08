import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

homes = []
chickens = []

for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            homes.append((r, c))
        elif board[r][c] == 2:
            chickens.append((r, c))

selected = [] 
ans = float('inf')

def backtracking(idx, count):
    global ans
    
    if count == m:
        total_dist = 0

        for hr, hc in homes:
            min_dist = float('inf')
            for cr, cc in selected:
                dist = abs(hr - cr) + abs(hc - cc)
                min_dist = min(min_dist, dist)
            total_dist += min_dist

        ans = min(ans, total_dist)
        return


    for i in range(idx, len(chickens)):
        selected.append(chickens[i]) 
        backtracking(i + 1, count + 1)
        selected.pop() 

backtracking(0, 0)
print(ans)