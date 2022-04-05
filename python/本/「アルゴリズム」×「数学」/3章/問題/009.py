import random

N = 10000000
M = 0

for i in range(N):
	px = random.random()
	py = random.random()

	#円周 x^2+y^2=r^2
	if px * px + py * py <= 1:
		M += 1

print(4*M/N)