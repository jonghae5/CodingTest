import sys
from collections import deque
import itertools as it


if __name__ == "__main__":

    n,time = map(int,input().split())

    res = [0] * (time+1)

    for i in range(n):
        a,b = map(int,input().split())
        for j in range(time,b-1,-1):
            res[j] = max(res[j],res[j-b] + a)
    print(max(res))