import sys
from collections import deque

def DFS(r,c,L):
    global ch
    if res[r][c] ==0:
        return

    if r<0 or c <0 or r>9 or c>9:
        return


    if r ==9 :
        cnt[L] +=1
        if cnt[L] == 1 and res[r][c] ==2:
            print(L)
            sys.exit(0)
    else:
        for i,j in [[0,-1],[0,1],[1,0]]: # 왼 오 아래
            if (r+i) < 0 or (c+j) <0 or (r+i) > 9 or (c+j) > 9:
                continue
            if ch[r+i][c+j] == 0 and res[r+i][c+j]>0:
                ch[r+i][c+j] = 1
                DFS(r+i,c+j,L)
                ch[r][c + j] =  0


if __name__ == "__main__":
    res = [list(map(int,input().split())) for _ in range(10)]

    cnt = [0] * 10

    for L in range(10):
        ch = [[0] * 10 for _ in range(10)]
        DFS(0,0+L,L)

