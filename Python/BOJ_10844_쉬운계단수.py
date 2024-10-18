N = int(input())

dp = [[0]*10 for _ in range(0,N+1)]

# print(dp)
tmp = [0]
tmp.extend([1]*9)
dp[1] = tmp
# print(tmp)

for n in range(2, N+1):
    for k in range(0,10):
        if k==0 :
            dp[n][k] = dp[n-1][k+1]
        elif k==9:
            dp[n][k] = dp[n-1][k-1]
        else:
            dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]
        # print(dp)

res = sum(dp[N])
print(res % 1000000000)