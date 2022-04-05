N = int(input())
T = list(input())

direct = "East"
now = [0, 0]

for i in range(N):
    if T[i] == "S":
        now_x = now[0]
        now_y = now[1]

        if direct == "East":
            now = [now_x + 1, now_y]
        elif direct == "West":
            now = [now_x - 1, now_y]
        elif direct == "North":
            now = [now_x, now_y + 1]
        elif direct == "South":
            now = [now_x, now_y - 1]
    else:
        if direct == "East":
            direct = "South"
        elif direct == "South":
            direct = "West"
        elif direct == "West":
            direct = "North"
        elif direct == "North":
            direct = "East"

print(now[0], now[1])