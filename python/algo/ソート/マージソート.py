from collections import deque

def solve(A):
    if len(A) <= 1:
        return A
    #準備
    X = len(A) // 2
    #1
    L = solve(A[:X])
    #2
    R = solve(A[X:])

    #3/4
    L += reversed(R)
    #5
    q = deque(L)
    B = []

    while(q):
        #e_firts <= e_last
        if q[0] <= q[-1]:
            f = q.popleft()
            B.append(f)
        #e_first > e_last
        else:
            e = q.pop()
            B.append(e)

    return B

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = solve(A)

    print(*ans)

if __name__ == "__main__":
    main()