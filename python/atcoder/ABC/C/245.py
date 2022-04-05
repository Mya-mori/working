N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

# dp表を作成
dp = [[False] * N for _ in range(2)]

#既知の範囲埋める
dp[0][0] = True
dp[1][0] = True


for i in range(N - 1):
    #A行を更新
    if dp[0][i] == True:
        #|A[i] - A[i+1]| <= K
        if abs(A[i] - A[i + 1]) <= K:
            dp[0][i + 1] = True

        #|B[i] - B[i+1]| <= K
        if abs(A[i] - B[i + 1]) <= K:
            dp[1][i + 1] = True
    #B行を更新
    if dp[1][i] == True:
        #|B[i] - B[i+1]| <= K
        if abs(B[i] - B[i + 1]) <= K:
            dp[1][i + 1] = True

        #|A[i] - A[i+1]| <= K
        if abs(B[i] - A[i + 1]) <= K:
            dp[0][i + 1] = True

if dp[0][N - 1] == True or dp[1][N - 1] == True:
    print("Yes")
else:
    print("No")
