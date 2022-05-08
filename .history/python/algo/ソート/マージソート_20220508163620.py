from collections import deque

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
    L += reversed(R)

    #5
    q = deque(L)
    B = []
    print(q)

print(solve(A))