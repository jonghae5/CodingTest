import sys
from collections import deque
import itertools as it

n = int(input())
result = []
for _ in range(n):
    a,h,w = map(int,input().split())
    result.append((a,h,w))
result.sort(reverse=True)


res = [0] * (n+1)
# 높이 저장하는 곳

for i in range(n):
    tmp_height = result[i][1]
    tmp_area = result[i][0]
    tmp_weight = result[i][2]
    maxx = 0
    for j in range(i):
        if (result[j][0] > tmp_area) and (result[j][2] > tmp_weight) :
            maxx = max(res[j],maxx)
    res[i] = maxx + tmp_height


print(max(res))
