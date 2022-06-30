def solve():
    N, W = map(int, input().split())
    A = list(map(int, input().split())) + [0, 0]
    good = [False] * (W + 1)

    for k in range(N + 2):
        for j in range(k):
            for i in range(j):
                w = A[i] + A[j] + A[k]
                if w <= W:
                    good[w] = True
    return good.count(True)

print(solve())