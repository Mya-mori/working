'''
A匹
K倍に増殖
B匹以上になるまで
'''
A, B, K = map(int, input().split())
ans = 0

for i in range(1000000):
    if A >= B:
        break
    else:
        A = A * K
        ans += 1

print(i)