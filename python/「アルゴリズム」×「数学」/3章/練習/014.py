N = int(input())

answer = []
LIMIT = int(N ** 0.5)
for i in range(2, LIMIT + 1):
	while N % i == 0:
		N /= i
		answer.append(i)
if N >= 2:
	answer.append(int(N))

print(answer)