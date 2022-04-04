# (0, 0) → (A, B)
# 原点Oから点(A, B)の距離はsqrt(A^2 + B^2)
# この長さ１の一ベクトルは(A/sqrt(A^2 + B^2), B/sqrt(A^2 + B^2))

A, B = map(int, input().split())
d = (A**2 + B**2) ** 0.5
a, b = A / d, B / d
print(a, b)