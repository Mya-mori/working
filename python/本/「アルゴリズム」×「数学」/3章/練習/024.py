#3.7.6
#dp[i] += dp[i-2]

N = int(input())
A = list(map(int, input().split()))

#i日目に勉強する配列
dp1 = [None] * (N + 1)
#i日目に勉強しない配列
dp2 = [None] * (N + 1)
#初期値は0
dp1[0] = 0
dp2[0] = 0

###### 考え方 #####
#i日目に勉強する
#dp1[i] = dp2[i-1] + A[i - 1]

#i日目に勉強しない
#dp2[i] = max(dp1[i-1], dp2[i-1])
#1. i-1日目に勉強しない (勉強しない日を+1する)
#2. i-1日目に勉強する
##################

for i in range(1, N + 1):
	dp1[i] = dp2[i - 1] + A[i - 1]
	dp2[i] = max(dp1[i - 1], dp2[i - 1])

ans = max(dp1[N], dp2[N])
print(ans)