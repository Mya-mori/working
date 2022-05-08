from audioop import reverse


N = int(input())
A = list(map(int,input().split()))

def solve(A):
    #準備
    X = len(A)//2
    #1
    L = A[:N//2]
    #2
    R = A[N//2:]

    #3
    L = solve(L)
    R = solve(R)

    #4
    L += reverse(R)

    #5
    B = []