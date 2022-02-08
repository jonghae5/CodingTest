import sys
from collections import deque


n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]

queue = deque()
direct = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] # 동 남 서 북 오위 오밑 왼밑 왼위
result = []

for i in range(n):
    for j in range(n):
        if res[i][j] == 1:
            cnt=1
            res[i][j] = 0
            queue.append((i,j))
            while queue:
                row,col = queue.popleft()
                for l,m in direct:
                    row +=l
                    col +=m
                    if row < 0 or col < 0 or row > n-1 or col > n-1:
                        row -=l
                        col -=m
                        continue
                    if res[row][col] == 1:
                        res[row][col] = 0
                        cnt +=1
                        queue.append((row,col))
                    row -= l
                    col -= m
            result.append(cnt)


print(len(result))