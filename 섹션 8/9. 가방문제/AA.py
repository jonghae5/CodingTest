import sys
from collections import deque
import itertools as it


if __name__ == "__main__":

    n, weight = map(int,input().split())
    result = [0] * (weight+1)
    # 보석 무게, 값어치

    for i in range(n):
        a,b = map(int,input().split())
        for j in range(a,weight+1):
            result[j] = max(result[j],result[j-a]+b)
    print(result[weight])
