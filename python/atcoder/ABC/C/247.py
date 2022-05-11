import sys
sys.setrecursionlimit(1000)

n = int(input())

def solve(N):
    if N == 1:
        return "1"
    else:
        return str(solve(N - 1)) + " "+ str(N) + " " + str(solve(N - 1))

print(solve(n))