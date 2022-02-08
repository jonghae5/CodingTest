import sys
from collections import deque
import itertools as it

n = int(input())
res = list(map(int,input().split()))
final = 0

result = [0] * (n+1)

for i in range(n):
    result[i] = 1
    maxx = 0
    for j in range(i):
        if res[j] < res[i] and result[j] > maxx:
            maxx = result[j]
    result[i] += maxx

print(max(result))


