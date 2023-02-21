N = int(input())
ARR = list(map(int,input().split()))

dp = [1] * N

for i in range(1,N):
    for j in reversed(range(i)):
        if ARR[j] < ARR[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
print(max(dp))