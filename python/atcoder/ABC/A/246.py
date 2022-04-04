X, Y = [], []
for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ax, ay = 0, 0

for i in range(3):
    if X.count(X[i]) == 1:
        ax = X[i]
    if Y.count(Y[i]) == 1:
        ay = Y[i]
print(ax, ay)