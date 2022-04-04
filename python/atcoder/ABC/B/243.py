N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#値も位置も一致
count_1 = 0
for i in range(N):
	if A[i] == B[i]:
		count_1 += 1

#値はあるが位置が異なる
List = set(A) & set(B)
count_2 = len(List)

print(count_1)
print(count_2 - count_1)