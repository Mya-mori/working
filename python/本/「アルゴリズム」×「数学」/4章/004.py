# 40
# 1, 2, .... , N
# A_1, A_2, .... , A_N-1
# M
# B_1 → B_M

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [0] * M
for i in range(M):
	B[i] = int(input())

# 累積をとる
S = [0] * N
for i in range(1, N):
	S[i] = S[i - 1] + A[i - 1]

#回答
ans = 0
for i in range(M - 1):
	# if B[i] < B[i + 1]:
		ans += abs(S[B[i + 1] - 1] - S[B[i] - 1])
	# else:
	# 	ans += S[B[i] - 1] - S[B[i + 1] - 1]

print(ans)