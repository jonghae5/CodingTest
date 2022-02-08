
import sys
from collections import deque


def DFS(x,y):
    global cnt
    if (x,y)== (x_e,y_e):
        cnt+=1
    else:
        for row,col in [[0,1],[1,0],[0,-1],[-1,0]]: # 동 남 서 북
            if x+row < 0 or y+col < 0 or x+row > n-1 or y+col > n-1:
                continue
            if res[x][y] < res[x+row][y+col]:
                DFS(x+row,y+col)



if __name__ == "__main__":
    n = int(input())
    res = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0
    maxx = 2147000000
    minn = -2147000000
    for i in range(n):
        for j in range(n):
            if maxx>res[i][j]:
                maxx = res[i][j]
                x_s,y_s = i,j

            elif minn < res[i][j]:
                minn = res[i][j]
                x_e,y_e = i,j

    # print(x_s,y_s)
    # print(x_e, y_e)

    DFS(x_s,y_s)
    print(cnt)
