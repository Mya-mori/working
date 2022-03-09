# p142
# 入力
N, Q = map(int, input().split())
L = [None] * Q #左の区間
R = [None] * Q #右の区間
X = [None] * Q #降雪量
for i in range(Q):
	L[i], R[i], X[i] = map(int, input().split())

#降雪量の累積
B = [0] * (N + 2)
for i in range(Q):
	B[L[i]] += X[i]
	B[R[i] + 1] -= X[i]

#結果
ans = ""
for i in range(2, N + 1):
	if B[i] > 0:
		ans += "<"
	elif B[i] == 0:
		ans += "="
	elif B[i] < 0:
		ans += ">"

print(ans)