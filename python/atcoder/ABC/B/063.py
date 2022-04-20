s = input()

#sの文字数分だけループ
for i in range(len(s)):
    if s.count(s[i]) != 1:
        print('no')
        exit()     #プログラムの終了
print('yes')

'''
str.count(sub[, start[, end]])
strの部分文字列subを検索し、その文字列が含まれる回数を返す.
'''