N = int(input())
A = list(map(int, input().split()))

#軸なる桁
for k in range(N - 1):
    min = A[k]
    j = k
    for i in range(k + 1, N):
        if A[i] < min:
            min = A[i]
            j = i
    A[k], A[j] = A[j], A[k]
    print(*A)