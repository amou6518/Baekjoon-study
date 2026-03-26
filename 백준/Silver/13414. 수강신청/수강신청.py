import sys
input = sys.stdin.readline

n,m = map(int, input().split())
table = dict()
for i in range(m):
  x = input().rstrip()
  if x in table:
    table.pop(x)
  table[x] = 1

print(*list(table.keys())[:n], sep="\n")