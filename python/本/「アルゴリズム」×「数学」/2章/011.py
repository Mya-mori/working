N = int(input())
ans = []

for i in range(2, N+1):
	tmp = 0
	#自身以外の数字をcount 1なら素数
	for j in range(2, i+1):
		if i % j == 0:
			tmp += 1
	if tmp == 1:
		ans.append(i)
#print(*A)
#各要素が空白でプロットされる
print(*ans)