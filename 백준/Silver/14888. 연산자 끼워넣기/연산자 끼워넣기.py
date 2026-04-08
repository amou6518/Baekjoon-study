import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_val = -1e9
min_val = 1e9

def dfs(idx, current_sum, add, sub, mul, div):
    global max_val, min_val
    
    if idx == n:
        max_val = max(max_val, current_sum)
        min_val = min(min_val, current_sum)
        return

    if add > 0:
        dfs(idx + 1, current_sum + numbers[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, current_sum - numbers[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, current_sum * numbers[idx], add, sub, mul - 1, div)
    if div > 0:
        if current_sum < 0:
            next_sum = -(-current_sum // numbers[idx])
        else:
            next_sum = current_sum // numbers[idx]
        dfs(idx + 1, next_sum, add, sub, mul, div - 1)

dfs(1, numbers[0], add, sub, mul, div)

print(int(max_val))
print(int(min_val))