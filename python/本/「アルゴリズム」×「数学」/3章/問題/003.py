#約数を出力する

N = int(input())

LIMIT = int(N ** 0.5)
divisors = []
for i in range(1, LIMIT+1):
	if N % i == 0:
		divisors.append(i)
		if i != N // i:
			divisors.append(N // i)

divisors.sort()
for i in divisors:
	print(i)