N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
S = sum(A)
#得票数Aが(1/4*M)未満
if A[M-1] >= S/(4*M):
    print("Yes")
else:
    print("No")