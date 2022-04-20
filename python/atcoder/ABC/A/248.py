'''
S 0から9の数字
1つを取り除く
'''

S = input()
ans = [i for i in range(10)]

for i in range(len(S)):
    ans.remove(int(S[i]))
print(int(ans[0]))