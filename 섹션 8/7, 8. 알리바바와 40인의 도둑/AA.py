import sys
from collections import deque
import itertools as it

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
ch[0][0] = board[0][0]

for j in range(1,n):
    ch[0][j] = ch[0][j-1] + board[0][j]
    ch[j][0] = ch[j - 1][0] + board[j][0]

for i in range(1,n):
    for j in range(1,n):
        ch[i][j] = min(ch[i][j-1],ch[i-1][j]) + board[i][j]

print(ch[n-1][n-1])


# def DFS(x,y):
#     if ch[x][y] > 0:
#         return ch[x][y]
#     if x==0 and y ==0 :
#         return ch[0][0]
#     else:
#         if x == 0 :
#             ch[x][y] = DFS(x,y-1) + board[x][y]
#         elif y == 0:
#             ch[x][y] = DFS(x-1,y) + board[x][y]
#         else:
#             ch[x][y] = min(DFS(x-1,y),DFS(x,y-1)) + board[x][y]
#         return ch[x][y]
#
#
#
#
#
# if __name__ =="__main__":
#     n = int(input())
#
#     board = [list(map(int, input().split())) for _ in range(n)]
#     ch = [[0] * n for _ in range(n)]
#     ch[0][0] = board[0][0]
#
#     print(DFS(n-1,n-1))