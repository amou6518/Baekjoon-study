import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1 
    for j in range(1, i + 1):
        if j == i:
            dp[i][j] = 1 
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k])