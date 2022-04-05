N, S = list(map(int, input()))
A = list(map(int, input().split()))

#最初No
ans = "No"
#0から2^Nパターン
for i in range(0, 1<<N):
	partsum = 0
	#Nまでのループ
	for j in range(0, N):
		#
		if (i & (1 << j)) != 0:
			partsum += A[j]
	if partsum == S:
		ans = "Yes"
		break

print(ans)

#>>> 1 << 2
# 4
#>>> 1 << 3
# 8
#>>> 1 << 4
# 16
#
#andと&は同じ