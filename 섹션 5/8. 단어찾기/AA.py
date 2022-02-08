
from collections import deque
'''오종해 풀이'''

n= int(input())

res = dict()

for _ in range(n):
    tmp = input()
    res[tmp] = 0

for _ in range(n-1):
    tmp = input()
    if tmp in res.keys():
        res[tmp] +=1

for keys,values in res.items():
    if res[keys] == 0:
        print(keys)
        break

# ''' 강의 풀이'''
#
# n = int(input())
# p = dict()
# for i in range(n):
#     word = input()
#     p[word] = 1
#
# for i in range(n-1):
#     word = input()
#     p[word] = 0
#
# for key, val in p.items():
#     if val ==1:
#         print(key)
#         break

