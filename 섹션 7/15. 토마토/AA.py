import sys
from collections import deque

m,n = map(int,input().split()) # 6 가로 4 세로
res = [list(map(int,input().split())) for _ in range(n)]
board = [[0]* m for _ in range(n)]
direct = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북
queue = deque()
cnt = 0

for i in range(n):
    for j in range(m):
        if res[i][j] == 1:
            queue.append((i,j))

# 모두 다 익어있는 경우
if len(queue) == (n*m):
    print(0)
    sys.exit(0)


while queue:
    row,col = queue.popleft()
    for l,k in direct:
        row += l
        col += k

        if row < 0 or col < 0 or row > n-1 or col > m-1:
            row -= l
            col -= k
            continue
        elif res[row][col] == 0 :

            board[row][col] = (board[row-l][col-k] + 1)
            res[row][col] = 1

            queue.append((row,col))

        row -= l
        col -= k
maxxx = 0
for i in range(n):
    for j in range(m):
        if res[i][j] == 0:
            print(-1)
            sys.exit(0)
        elif board[i][j] > maxxx:
            maxxx =board[i][j]


print(maxxx)