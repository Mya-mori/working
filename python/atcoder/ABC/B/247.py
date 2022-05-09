from unicodedata import name


N = int(input())

#姓リスト
s_list = []
#名リスト
t_list = []

for i in range(N):
    s, t = map(str, input().split())

    s_list.append(s)
    t_list.append(t)

# 名前のリスト
for i in range(N):
    namelist = []
    #i != k である名前リストを作成
    for k in range(N):
        if i != k:
            namelist.append(s_list[k])
            namelist.append(t_list[k])

    if s_list[i] in namelist and t_list[i] in namelist:
        print("No")
        exit()

print("Yes")