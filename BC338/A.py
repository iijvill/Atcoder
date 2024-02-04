from sys import stdin
input = stdin.readline

S = input().rstrip()
res = S.istitle()

print('Yes' if res else 'No')
