n, k=map(int,input().split())

dp = [[0] * (201) for _ in range(201)]

dp[0][0] = 1

for i in range(0, 201):
    for j in range(1,201):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 

print(dp[n][k]% 1000000000)

