def solve():
    #シミュレーション
    def calc(p, q, r):
        t = 0 #時間
        dist = 0 #距離
        while True:
            #p秒間歩く
            for _ in range(p):
                t += 1
                dist += q
                if t == x:
                    return dist
            #r秒間休む
            for _ in range(r):
                t += 1
                if t == x:
                    return dist
    a, b, c, d, e, f, x = map(int, input().split())
    ta = calc(a, b, c)
    ao = calc(d, e, f)
    if ta == ao:
        return "Draw"
    elif ta > ao:
        return "Takahashi"
    else:
        return "Aoki"

print(solve())