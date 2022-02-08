import sys
from collections import deque
import itertools as it

def DFS(L):
    global cnt
    if L ==1:
        res[L] = 1
        return
    elif L==2:
        res[L] = 2
        return
    elif res[L] != 0:
        return
    else:
        DFS(L-1)
        DFS(L-2)
        res[L] = res[L - 1] + res[L - 2]

if __name__ =="__main__":
    n = int(input())
    res = [0] * (n+1)
    DFS(n)
    print(res[-1])

# if __name__ =="__main__":
#     n = int(input())
#     result = [0] * (n+1)
#     result[0] = 1
#     result[1] = 1
#
#     for i in range(1,n):
#         result[i+1] = result[i] + result[i-1]
#
#     print(result[n])