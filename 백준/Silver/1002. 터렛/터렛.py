import sys

def circle():
    line = sys.stdin.readline().split()
    if not line: return
    x1, y1, r1, x2, y2, r2 = map(int, line)
    
    dist_sq = (x1 - x2)**2 + (y1 - y2)**2
    
    sum_r_sq = (r1 + r2)**2
    diff_r_sq = (r1 - r2)**2
    
    if dist_sq == 0 and r1 == r2:
        print(-1)
    elif dist_sq == sum_r_sq or dist_sq == diff_r_sq:
        print(1)
    elif diff_r_sq < dist_sq < sum_r_sq:
        print(2)
    else:
        print(0)

t = int(sys.stdin.readline())
for _ in range(t):
    circle()