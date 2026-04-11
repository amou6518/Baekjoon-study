import sys

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
else:
    opinions = []
    for _ in range(n):
        opinions.append(int(input()))
    opinions.sort()
    trim_count = my_round(n * 0.15)

    target_opinions = opinions[trim_count : n - trim_count]
    
    if not target_opinions:
        print(0)
    else:
        avg = sum(target_opinions) / len(target_opinions)
        print(my_round(avg))