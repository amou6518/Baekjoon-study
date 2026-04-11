import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
else:
    cnt = 1     
    max_num = 1 
    while n > max_num:
        max_num += 6 * cnt
        cnt += 1
        
    print(cnt)