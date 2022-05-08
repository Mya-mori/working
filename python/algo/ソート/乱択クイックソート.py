import random
TF = int(input())
A = list(map(int, input().split()))

def sort(array):
    #入力がない時は空のリストを返す
    if len(array) == 0:
        return []
    N = len(array)
    L = []
    R = []
    #randrange(start, stop, step)
    #start:開始点 stop:終了点 step:ステップ
    #randrange(2) → 0,1を返す
    X = random.randrange(N)

    for i in range(N):
        if i == X:
            continue
        elif array[i] < array[X]:
            L.append(array[i])
        elif array[i] > array[X]:
            R.append(array[i])
        elif array[i] == array[X]:
            if random.randrange(2):
                L.append(array[i])
            else:
                R.append(array[i])
    L = sort(L)
    R = sort(R)
    return L + [array[X]] + R

print(*sort(A))