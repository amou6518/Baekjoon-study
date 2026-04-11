import sys

input = sys.stdin.readline

n = int(input())
stack = []
ans = []
current = 1  
possible = True

for _ in range(n):
    target = int(input())
    while current <= target:
        stack.append(current)
        ans.append("+")
        current += 1
    
    if stack[-1] == target:
        stack.pop()
        ans.append("-")
    else:
        possible = False
        break

if possible:
    for op in ans:
        print(op)
else:
    print("NO")