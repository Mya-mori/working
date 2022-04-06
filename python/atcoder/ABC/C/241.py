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

# 入力の受け取り
N=int(input())

# マス目の情報格納用
grid=[]
# N回
for i in range(N):
    # 文字列で受け取り
    S=input()
    # リストへ展開
    S=list(S)
    # gridへ追加
    grid.append(S)

# 右方向へ「#」を数える
# 引数：行番号,列番号　→　返り値「#」の数
def SearchRight(gyou,retu):
    # 「#」の数
    count=0
    # i=0~5まで
    for i in range(6):
        # マス(行番号,列番号)=「#」ならば
        if grid[gyou][retu+i]=="#":
            # カウント
            count+=1
    # 数を返す
    return count

# 下方向
def SearchDown(gyou,retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu]=="#":
            count+=1
    return count

# 右下方向
def SearchRightDown(gyou,retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu+i]=="#":
            count+=1
    return count

# 左下方向
def SearchLeftDown(gyou,retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu-i]=="#":
            count+=1
    return count

# gyou=0~(N-1)
for gyou in range(N):
    # retu=0~(N-1)
    for retu in range(N):
        # 5マス右がマス目の中に収まっているならば
        if retu+5<N:
            # 「#」の数が4つ以上なら
            if 4<=SearchRight(gyou, retu):
                # 「Yes」を出力
                print("Yes")
                # 終了
                exit()

        # 5マス下がマス目の中に収まっているならば
        if gyou+5<N:
            if 4<=SearchDown(gyou, retu):
                print("Yes")
                exit()

        # 5マス右下がマス目の中に収まっているならば
        if retu+5<N and gyou+5<N:
            if 4<=SearchRightDown(gyou, retu):
                print("Yes")
                exit()

        # 5マス左下がマス目の中に収まっているならば
        if gyou+5<N and 0<=retu-5:
            if 4<=SearchLeftDown(gyou, retu):
                print("Yes")
                exit()

# 「No」を出力
print("No")