N = int(input())
P = [None] * N
Q = [None] * N
for i in range(N):
	P[i], Q[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
	ans += Q[i] / P[i]

print(ans)