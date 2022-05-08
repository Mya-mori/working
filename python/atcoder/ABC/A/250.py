H, W = map(int, input().split())
R, C = map(int, input().split())

count = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if abs(i - R) + abs(j - C) == 1:
            count += 1

print(count)