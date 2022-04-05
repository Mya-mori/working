N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

ans_b = 0
ans_r = 0
for i in range(N):
	ans_b += B[i]
	ans_r += R[i]

print((ans_b+ans_r)/N)