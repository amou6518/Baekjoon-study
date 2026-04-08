import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1]
    q = deque(arr.split(',') if n > 0 else [])

    rev = False
    error = False

    for AC in p:
        if AC == 'R':
            rev = not rev
        else: 
            if not q:
                error = True
                break
            q.pop() if rev else q.popleft()

    if error:
        print("error")
    else:
        if rev: q.reverse() 
        print(f"[{','.join(q)}]")