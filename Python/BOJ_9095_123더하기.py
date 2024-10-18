T = int(input())

n_list = [int(input()) for _ in range(T)]
m = max(n_list)

if m > 3 :
    dp = [0]*(m+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, m+1) :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
else :
    dp = [0,1,2,4]

for n in n_list:
    print(dp[n])
