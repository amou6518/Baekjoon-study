import sys

s = sys.stdin.readline().rstrip()

result = []
for i in range(97, 123):
    char = chr(i) 
    result.append(s.find(char))
print(*result)