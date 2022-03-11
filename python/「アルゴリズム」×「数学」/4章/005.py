# 4.2.2
#開店0時, 閉店T時
#N人従業員 出勤L, 退勤R
#従業員数を出力

#入力
#閉店
T = int(input())
#従業員の数
N = int(input())
#各従業員の稼働時刻
L = [0] * N
R = [0] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

A = [0] * (T + 2)
B = [0] * (T + 2)


for i in range(N):
	B[L[i]] += 1
	B[R[i]] -= 1

A[0] = B[0]
for i in range(1, T):
	A[i] = A[i - 1] + B[i]

for i in range(T):
	print(A[i])