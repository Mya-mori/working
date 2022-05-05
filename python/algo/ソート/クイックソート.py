N = int(input())
A = list(map(int,input().split()))

def quick_sort(array):
    # Xは(N/2)を基準とする
    X = N // 2
    if len(array) <= 1:
        return array
    # 
    L = []
    R = []
    for i,x in enumerate(array):
        if i!= X:
            if array[i]<array[X]:
                L.append(array[i])
            else:
                R.append(array[i])
    L = quick_sort(L)
    R = quick_sort(R)
    return [*L,array[X],*R]

print(*quick_sort(A))