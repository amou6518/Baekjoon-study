import sys

def team():
    n = int(sys.stdin.readline())
    s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    visited = [False] * n
    min_diff = float('inf')

    def dfs(idx, count):
        nonlocal min_diff
        
        if count == n // 2:
            start_score, link_score = 0, 0
            for i in range(n):
                for j in range(n):
                    if visited[i] and visited[j]:
                        start_score += s[i][j]
                    elif not visited[i] and not visited[j]:
                        link_score += s[i][j]
            
            min_diff = min(min_diff, abs(start_score - link_score))
            return

        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(i + 1, count + 1)
                visited[i] = False 

    visited[0] = True
    dfs(1, 1)
    
    print(min_diff)

team()