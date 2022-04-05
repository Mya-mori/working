N = int(input())
A = list(map(int, input().split()))

cnt = [0 for i in range(100000)]
for i in range(N):
	cnt[A[i]] += 1

ans = 0
for i in range(1, 50000):
	ans += cnt[i] * cnt[100000 - i]
ans += cnt[50000] * (cnt[50000] - i) // 2

print(ans)