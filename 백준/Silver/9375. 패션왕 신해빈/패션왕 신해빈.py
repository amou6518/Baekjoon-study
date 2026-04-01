import sys

test = int(sys.stdin.readline())

for _ in range(test):
    n = int(sys.stdin.readline())
    clothes = {}
    
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
            
    answer = 1
    for count in clothes.values():
        answer *= (count + 1)
        
    print(answer - 1)