'''
<input>
・N 配列の長さ
・M 各要素1以上M以下の整列
・K 各要素の和がK以下
</input>

1. 候補となる配列を書き出す → タイムオーバー
2. DPっぽい

・dp[i][j]: i番目までに使った数の中で、j番目までに使った数の総和

・dp[N][1] + dp[N][2] + ... + dp[N][K]

初期値:
dp[0][0] = 1

遷移:
dp[i][j] → dp[i + 1][j]
1 <= [i + 1] <= K

[i + 1]行目で, [j + k]の総和

dp[i + 1][j + k] = dp[i][j]
'''
#1
#回答用
# MOD = 998244353

# #input
# N, M, K = map(int, input().split())

# #初期配列の作成
# dp = [[0] * (K + 1) for _ in range(N + 1)]
# # print([0] * (K + 1)) 5列
# # print(dp) 3*5の配列

# #初期値
# dp[0][0] = 1

# #i(1~N)行目
# for i in range(N):
#     #j(1~K)列目
#     for j in range(K):
#         #K 各要素の数
#         for k in range(1, M+1):
#             #j + k
#             if j + k > K:
#                 break
#             dp[i + 1][j + k] += dp[i][j]
#             dp[i + 1][j + k] %= MOD
# print(sum(dp[-1]) % MOD)

#2

'''
1行目
X <= M
→ dp[1][x] = 1
X > M
→ dp[1][x] = 0
'''

N, M, K = map(int, input().split())

MOD = 998244353

#初期表
dp = [[0]*(K + 1) for i in range(M + 1)]

#わかるところ
#x <= M dp[1][x] = 1
#x > M dp[1][x] = 0
for x in range(1, M + 1):
    dp[1][x] = 1

#小さいところから
#i=2~N
for i in range(2, N + 1):
    for x in range(1, K + 1):
        for a in range(x - M, x):
            #aが1未満
            if a < 1:
                continue
            #(2<=i<=N)
            #dp[i][x] += dp[i-1][x-M]~dp[i-1][x-1]の和
            dp[i][x] += dp[i - 1][a]
            dp[i][x] %= MOD
ans = 0

for x in range(1,K + 1):
    # dp[N][1]~dp[N][K]の和
    ans += dp[N][x]
    # 余りを取る
    ans %= MOD

# 答えを出力
print(ans)