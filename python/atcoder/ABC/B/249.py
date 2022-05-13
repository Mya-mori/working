def judge():
    S = input()
    # print("S: ", S)
    # islower 全て小文字かを判断(全て大文字なら True)
    # not S.islower() 大文字があるなら True
    b1 = not S.islower()
    # print("S not islower:", b1)
    # isupper 全て大文字かを判断
    # not S.isupper() Sに小文字が含まれているなら True
    b2 = not S.isupper()
    # print("S not isupper:", b2)
    b3 = len(S) == len(set(S))
    print(b1 and b2 and b3)
    return b1 and b2 and b3

print("Yes" if judge() else "No")