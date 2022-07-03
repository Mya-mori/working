import heapq
a = [1, 6, 8, 0, -1]
a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
print(a)

heapq.heapify(a)
print(heapq.heappop(a)*(-1))  # 最大値の取り出し
print(a)