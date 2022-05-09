#解法1
N = list(input())

N.pop()
N.insert(0, "0")
N = "".join(N)
print(N.strip())

#解法2
S = input()
print(f"0{S[:3]}")  # fstring