#3.6.6

def func(N):
	return func(N-1) * N

N = int(input())
print(func(N))