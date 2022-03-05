#3.7.3

N, W = map(int, input().input())
w = [None] * N
v = [None] * N
for i in range(N):
	w[i], v[i] = map(int, input().split())

#配列の初期化
INF = 10 ** 10
dp = [[None] * (W + 1) for i in range(N + 1)]
#最初は何も持っていない
dp[0][0] = 0
#品目0は重さが1以上にならない
for i in range(1, W+1):
	dp[0][i] = -INF


for i in range(1, N + 1):
	for j in range(1, W + 1):
		if j < W[i - 1]:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1] + v[i - 1]])
			
answer = max(dp[N])
print(answer)