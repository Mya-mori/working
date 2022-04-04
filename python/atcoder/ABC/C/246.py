"""
input
N 商品数
A i番目の商品お値段
K クーポンの枚数
X 値引きの額
"""

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
rem = K #クーポンお残り枚数
Q = sum(x // X for x in A)  #値引き可能回数
R = sorted((x % X for x in A), reverse=True) #値引き後のあまりを降順にソート
ans -= X * min(Q, rem) #Qかクーポン枚数が小さい方を使う
rem -= min(Q, rem) #使用した分を減らす
ans -= sum(R[:rem]) #クーポン枚数が小さい方を使う
print(ans)