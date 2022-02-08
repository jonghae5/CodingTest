import sys
from collections import deque
import itertools as it



if __name__ == "__main__":

    n = int(input())
    coin = list(map(int, input().split()))
    change = int(input())
    res = [0] * (change+1)
    for i in range(n):
        a = coin[i]
        for j in range(a,change+1):
            if res[j] == 0 :
                res[j] = max(res[j],res[j-a] + 1)
            else:
                res[j] = min(res[j],res[j-a] + 1)

    print(res[change])