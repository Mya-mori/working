N = int(input())
A = list(map(int, input().split()))

for k in range(1, N):
    #1. posにkを代入
    pos = k
    #2. pos != 0 かつ A[pos - 1] < A[pos]
    while pos != 0 and A[pos - 1] >= A[pos]:
        #3. A[pos - 1]とA[pos]を交換
        tmp = A[pos - 1]
        A[pos - 1] = A[pos]
        A[pos] = tmp
        #4. posを1減らす
        pos -= 1
    print(*A)