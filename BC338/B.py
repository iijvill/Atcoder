from sys import stdin
import collections

input = stdin.readline

S = input().rstrip()

strList = list(S) #配列化

counter = collections.Counter(strList) #各要素の出現数を出す

most = counter.most_common()
maxStr = []
maxCnt = 0
for t in most:
  if t[1] >= maxCnt:
    maxCnt = t[1]
    maxStr.append(t[0])
print(sorted(maxStr)[0])
