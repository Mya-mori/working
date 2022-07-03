'''
・H行W列 2つのマスに駒がある
・Si_j = o → i行目j列目に駒がある
・Si_j = - → i行目j列目に駒がない

・2つの駒が同一座標になるためには何回移動が必要か
'''

H, W = map(int, input().split())
S = [input() for i in range(H)]
P = []

for row in range(H):
    for col in range(W):
        if S[row][col] == "o":
            P.append((row, col))

ar, ac = P[0]
br, bc = P[1]

ans = abs(ar - br)  + abs(ac - bc)
print(ans)