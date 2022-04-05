# 入力の受け取り
N=int(input())

# すでに使った数の記録
used=[False]*(2*N+2)

# 最初は「1」を出力
print(1)
# 「1」は使用済み
used[1]=True

# N回
for i in range(N+1):
    # 青木くんの入力を受け取り
    x=int(input())
    # 「x」は使った
    used[x]=True

    # x=「0」の場合
    if x==0:
        # 終了
        exit()

    # k=1~(2k+1)
    for k in range(1,2*N+2):
        # まだ使っていないなら
        if used[k]==False:
            # 「k」を出力
            print(k)
            # 「k」は使った
            used[k]=True
            # forループを抜ける
            break