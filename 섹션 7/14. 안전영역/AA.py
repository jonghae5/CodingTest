import sys
from collections import deque


n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
res_copy = res.copy()
queue = deque()
direct = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북 오위 오밑 왼밑 왼위

result = set()

minn = min(min(res))
maxx = max(max(res))


for h in range(minn,maxx):

    queue = deque()
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if res[i][j] > h and ch[i][j] == 0:
                ch[i][j] = 1
                queue.append((i,j))
                cnt += 1
                while queue:
                    row,col = queue.popleft()
                    for l,m in direct:
                        row+=l
                        col+=m
                        if row < 0 or col < 0 or row > n-1 or col > n-1:
                            row-=l
                            col-=m
                            continue
                        if res[row][col] > h and ch[row][col] == 0:
                            queue.append((row, col))
                            ch[row][col] = 1

                        row-=l
                        col-=m

    result.add(cnt)

print(max(result))
