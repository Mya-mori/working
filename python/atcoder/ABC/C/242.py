###############################################
N, W = map(int, input().split())

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(1, N+1):
	wi, vi = map(int, input().split())

	for w in range(W+1):
		if w - wi < 0:
			dp[i][w] = dp[i - 1][w]
		else:
			dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)

print(dp[N][W])
###############################################

#あまりの定義
mod = 998244353

#入力
N = int(input())

#初期値
dp = [[0]*10 for i in range(N+1)]

#1桁の時を埋める
for i in range(1, 10):
	dp[1][i] = 1

#小さい順に埋めていく
for d in range(2, N+1):
	#i=1~9
	for i in range(1, 10):
		#2<=d, i=1
		if i == 1:
			dp[d][i] = dp[d - 1][i] +dp[d - 1][i + 1]
		
		#2<=d, 2<i<9
		elif 2 <= i <= 8:
			dp[d][i] = dp[d - 1][i - 1] + dp[d - 1][i] + dp[d - 1][i + 1]
		
		#2<=d, i=9
		else:
			dp[d][i] = dp[d - 1][i - 1] + dp[d - 1][i]

		dp[d][i] %= mod
print(sum(dp[1]))
ans = sum(dp[N]) % mod
print(ans)