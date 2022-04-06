from collections import Counter
"""
< Counter >
import collections
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True
"""

def solve():
    N, M = map(int, input().split())
    A = Counter(map(int, input().split()))
    print("A", A)
    print("A[1]", A[3])
    B = list(map(int, input().split()))
    print("B", B)
    for x in B:
        if A[x] == 0:
            return False
        A[x] -= 1
    return True
print("Yes" if solve() else "No")