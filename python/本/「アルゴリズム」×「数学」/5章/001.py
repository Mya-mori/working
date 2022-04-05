#059
#2^Nの1の位を求める

N = int(input())
if N % 4 == 1:
    print(2)
if N % 4 == 2:
    print(4)
if N % 4 == 3:
    print(8)
if N % 4 == 0:
    print(6)