# 33 Distance p135
#A(a_x,a_y), B(b_x, b_y), C(c_x, c_y)
#pAとlBCの最短距離

import math

#入力
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

#内積の求め方
#A(a_x,a_y), B(b_x, b_y)
#a*b = a_x*b_x + a_y*b_y

#考え方
#点と線分の位置関係
#BA, BCの内積が負の場合 → 角が90°より大きい p1
#CA, CBの内積が負の場合 → 角が90°より大きい p2
#BA, BCの内積が正の場合 → 両角が90°以下  p3

#各成分表示を求める
BAx, BAy  =  ax - bx, ay - by
BCx, BCy  =  cx - bx, cy - by
CAx, CAy  =  ax - cx, ay - cy
CBx, CBy  =  bx - cx, by - cy

#内積からパターンを求める
if BAx * BCx + BAy * BCy < 0:
	p = 1
elif CAx * CBx + CAy * CBy < 0:
	p = 2
else:
	p = 3

if p == 1:
	ans = math.sqrt(BAx ** 2 + BAy ** 2)
if p == 2:
	ans = math.sqrt(CAx ** 2 + CAy ** 2)
if p == 3:
	s = abs(BAx * CAy - BAy * CAx)
	length = math.sqrt(BCx ** 2 + BCy ** 2)
	ans = s / length

print("%.12f" % ans)