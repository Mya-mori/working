#3.6.3　再帰 階乗

def func(N):
	if N == 1:
		return 1
	return func(N-1)*N

N = int(input())
print(func(N))