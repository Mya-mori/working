#3.7.2

#入力
N = int(input())

#箱
dp = [None] * (N+1)

#0~N番目まで
for i in range(N+1):
	#0番目(スタート地点)からi=1段目に上がるのは1通り
	#2段目以降は場合分け
	#N段目登るのにN-1段目から登る
	#N段目登るのにN-2段目から登る
	if i <= 1:
		dp[i] = 1
	else:
		dp[i] = dp[i-1] + [i-2]

print(dp[N])