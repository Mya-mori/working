"""
N・N
・・#・
・#・・
・#・・
・・#・

# →黒
・→白

2回黒に塗りつぶすことが可能
黒を6つ並べられるかを判定する

1. 連続する6マスを選択する
2. 選択した6マスの中に黒が4つ以上あるか
"""

N = int(input())
grid = [map(int, input().split()) for _ in range(N)]

#右方向に#を数える
def SearchRight(gyou, retu):
    # #の数
    count = 0
    for i in range(6):
        if grid[gyou][retu + i] == "#":
            count += 1
    return count

#下方向に#を数える
def SearchDown(gyou, retu):
    # #の数
    count = 0
    for i in range(6):
        if grid[gyou + i][retu] == "#":
            count += 1
    return count

#右下方向に#を数える
def SearchRightDown(gyou, retu):
    # #の数
    count = 0
    for i in range(6):
        if grid[gyou + i][retu + i] == "#":
            count += 1
    return count

#左下方向に#を数える
def SearchLeftDown(gyou, retu):
    # #の数
    count = 0
    for i in range(6):
        if grid[gyou + i][retu - i] == "#":
            count += 1
    return count

for gyou in range(N):
    for retu in range(N):
        #5マス右がマス目内にある
        if retu + 5 < N:
