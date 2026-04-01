import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    target_a, target_b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        parent, child = map(int, sys.stdin.readline().split())
        graph[parent].append(child)
        graph[child].append(parent)

    visited = [-1] * (n + 1)
    queue = deque([target_a])
    visited[target_a] = 0 
    
    while queue:
        current = queue.popleft()

        if current == target_b:
            print(visited[target_b])
            return
            
        for neighbor in graph[current]:
            if visited[neighbor] == -1: 
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)

    print(-1)

if __name__ == "__main__":
    solve()