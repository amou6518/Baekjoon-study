import sys

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

ans = []
for i in range(n):
    rank = 1 
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ans.append(str(rank))

print(" ".join(ans))