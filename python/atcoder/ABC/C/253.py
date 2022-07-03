'''
<問題>
・S 多重集合(初期はから集合)
・Q個のクエリ
    ・1 x  : Sにxを1つ追加する
    ・2 x c: Sからxをmin(c, (Sに含まれるxの数))個削除する
    ・3    : max(S) - min(S) を出力 [Sは空ではない]

<memo>
・defalutdictでそれぞれの数がSに入っている数を管理する
→ dict型で管理する
→ Sに「1」が3個 Count[1]=3
・heapで最大値、最小値を高速で取り出す
'''
Q = int(input())

from collections import defaultdict

#Sにいくつ入っているかを確認する
#初期値は0
Count = defaultdict(int)

import heapq

#最大値を取り出す
MaxQue = []
#最小値を取り出す
MinQue = []

for i in range(Q):
    query = list(map(int, input().split()))

    #クエリ1 xに1を追加
    if query[0] == 1:
        #例) [1, 3] 3をxに格納
        x = query[1]
        #1追加する
        Count[x] += 1
        #heap que
        heapq.heappush(MinQue, x)
        #heap que
        heapq.heappush(MaxQue, -x)

    #クエリ2 削除
    elif query[0] == 2:
        #x, cを確認
        x = query[1]
        c = query[2]
        #Sからxをmin(c, (Sに含まれるxの数))個削除する
        Count[x] -= min(c, Count[x])

    #クエリ3
    else:
        #最小値を取得する
        SMin = heapq.heappop(MinQue)
        #SMinが0個である場合
        while Count[SMin] == 0:
            #次の値を取得する
            SMin = heapq.heappop(MinQue)

        #最大値を取得する
        SMax = heapq.headpop(MaxQue)
        SMax *= -1
        #SMaxが0個である場合
        while Count[SMax]==0:
            # 次の最大値を取り出す
            SMax=heapq.heappop(MaxQue)
            # マイナスを取る⇔(-1)を掛ける
            SMax*=-1

        #(Max - Min)
        print(SMax - SMin)
        # 最小値、最大値をheap queへ戻す
        heapq.heappush(MinQue,SMin)
        heapq.heappush(MaxQue,-SMax)