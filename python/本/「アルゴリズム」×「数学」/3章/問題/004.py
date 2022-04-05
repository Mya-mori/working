#最大公約数を求める
def GCD(A, B):
	ans = 0
	for i in range(1, min(A, B)+1):
		if A % i == 0 and B % i == 0:
			ans = i
	return ans

A, B = map(int, input().split())
print(GCD(A, B))