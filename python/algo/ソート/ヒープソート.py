from re import X


def heaptree(A):
    #1
    n = len(A)
    x = n // 2 - 1

    #2
    while x >= 0:
        #2-1
        k = x
        #2-1-1
        while 2 * k + 1 < n:
            mx = max(A[k], A[2 * k + 1])
            if 2 * k + 2 < n:
                mx = max(mx, A[2 * k + 2])
            if A[k] == mx:
                break
            elif A[2 * k + 1] == mx:
                A[k], A[2 * k + 1] = A[2 * k + 1], A[k]
                k = 2 * k + 1
            else:
                A[k], A[2 * k + 2] = A[2 * k + 2], A[k]
                k = 2 * k + 2
        x -= 1
    return A

n = int(input())
A = list(map(int, input().split()))
print(*heaptree(A))