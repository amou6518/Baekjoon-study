import sys
N, M = map(int, sys.stdin.readline().split())
d = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    
    if (len(word) < M):
        continue
        
    if (word in d):
        d[word] += 1
    else:
        d[word] = 1

d = sorted(d.items(), key = lambda x : x[0])
d = sorted(d, key = lambda x : len(x[0]), reverse=True)
d = sorted(d, key = lambda x : x[1], reverse=True)

for i in d:
    print(i[0])