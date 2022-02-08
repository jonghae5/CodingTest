import sys
from collections import deque
import itertools as it

if __name__ == "__main__":
    n,m = map(int,input().split())

    board = [[0]*n for _ in range(n)]

    for _ in range(m):
        a,b = map(int,input().split())
        board[a-1][b-1] = 1

    # 진출 진입
    res = []
    ch = [0] * n
    while True:
        for i in range(n):
            for j in range(n):
                if board[j][i] > 0:
                    break
            else:
                if ch[i] ==0:
                    ch[i] = 1
                    res.append(i+1)
                    for k in range(n):
                        board[i][k] = 0
        if len(res) == n:
            break

    for x in res:
        print(x,end=' ')

