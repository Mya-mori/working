#父   A  F
#母   B  M
#本人 C  T

V, A, B, C = map(int, input().split())

for i in range(1000000000):
	if V < A:
		print("F")
		break
	else:
		V -= A
		if  V < B:
			print("M")
			break
		else:
			V -= B
			if V < C:
				print("T")
				break
			else:
				V -= C