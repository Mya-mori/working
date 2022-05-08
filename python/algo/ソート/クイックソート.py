def quick_sort(array):
    # Xは(N/2)を基準とする
    X = len(array) // 2
    L = []
    R = []

    for i in range(len(array)):
        if i == X:
            continue
        if array[i] < array[X]:
            L.append(array[i])
        else:
            R.append(array[i])
    if len(L) != 0:
        L = quick_sort(L)
    if len(R) != 0:
        R = quick_sort(R)
    return L + [array[X]] + R

N = int(input())
A = list(map(int,input().split()))
print(*quick_sort(A))