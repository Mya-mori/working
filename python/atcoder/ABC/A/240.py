#直線で結ばれている時
#数字が隣り合う時 or 1と最後の数字

A, B = map(int, input().split())
ans = "No"
if A + 1 == B:
	ans = "Yes"
elif A == 1 and B == 10:
	ans = "Yes"

print(ans)