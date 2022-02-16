#最大公約数を求める
def GCD(A,B):
	while A >= 1 and B >= 1:
		if A < B:
			B = B % A
		else:
			A = A % B
	if A >= 1:
		return A
	else:
		return B

#最小公倍数
def LCM(A, B):
	return  int(A/GCD(A, B)) * B

N = int(input())
A = list(map(int, input().split()))

print(R)