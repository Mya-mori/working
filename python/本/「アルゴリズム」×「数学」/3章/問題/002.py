#計算量O(N**0.5)

def isprime(N):
	LIMIT = int(N ** 0.5)
	for i in range(2, LIMIT+1):
		if N % i == 0:
			return False
	return True

N = int(input())
if isprime(N):
	print("prime")
else:
	print("not prime")