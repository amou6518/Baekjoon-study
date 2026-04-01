import sys

n = int(sys.stdin.readline())
target = 666
cnt = 0

while True:
    if '666' in str(target):
        cnt += 1 
    if cnt == n:
        print(target)
        break
    target += 1