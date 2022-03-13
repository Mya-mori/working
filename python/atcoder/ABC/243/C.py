#入力
N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
	X[i], Y[i] = map(int, input().split())
S = list(input())

#Y成分が同一かつ左がR, 右がLの時衝突が生じる
ans = False
for i in range(N): #X自分
	for j in range(i+1, N): #Y 他人
		if Y[i] == Y[j]: #Y成分が同一
			if X[i] < X[j]: #自分 他人
				if S[i] == "R" and S[j] == "L":
					ans = True
					break
			if X[i] > X[j]: #他人 自分
				if S[i] == "L" and S[j] == "R":
					ans = True
					break

if ans:
	print("Yes")
else:
	print("No")