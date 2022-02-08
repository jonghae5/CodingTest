import sys
from collections import deque
import itertools as it

if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [[10000]*n for i in range(n)]

    for idx in range(m):
        i,j,val = map(int,input().split())
        board[i-1][j-1] = val

    for k in range(n):
        for l in range(n):
            for m in range(n):
                if board[l][k] and board[k][m]:
                    board[l][m] = min(board[l][m],board[l][k] + board[k][m])

    for i in range(n):
        for j in range(n):
            if i ==j :
                board[i][j] = 0
                continue
            if board[i][j] == 10000:
                if i!=j:
                    board[i][j] = "M"
                else:
                    board[i][j] = 0

    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()



