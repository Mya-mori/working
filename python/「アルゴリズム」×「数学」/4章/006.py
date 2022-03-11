# p150 ニュートン法
# sqrt(2)
# f(x) = x^2
r = 2.0 #sqrt(2)を求める y=2
a = 2.0 #初期値 
event = 10

for i in range(1, event + 1):
	#p(a, f(a))の座標
	x, y = a, a * a

	#接戦の式
	#x^2を微分
	#a = 4
	a = 2.0 * x
	#b = -4
	b = y - a * x

	next_a = (r - b) / a
	print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
	a = next_a