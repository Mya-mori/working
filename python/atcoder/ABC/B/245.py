N = int(input())
A = list(map(int, input().split()))

for x in range(2001):
    if x not in A:
        print(x)
        exit()