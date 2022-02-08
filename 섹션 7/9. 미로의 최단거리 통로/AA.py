
import sys
from collections import deque

mapp = [list(map(int,input().split())) for _ in range(7)]
direct = [[0,1],[1,0],[-1,0],[0,-1]] # 동 남 서 북
queue = deque()
queue.append((0,0))
mapp[0][0] = -1
L = 1
while queue:
    for k in range(len(queue)):
        i,j = queue.popleft() # 좌표
        for row,col in direct:
            i += row
            j += col
            if i < 0 or j < 0 or i > 6 or j >6:
                i -= row
                j -= col
                continue
            elif mapp[i][j] == 0 :
                queue.append((i,j))
                mapp[i][j] = L
                if (i, j) == (6, 6):
                    print(mapp[i][j])
                    sys.exit(0)
            i -= row
            j -= col
    L+=1

print(-1)



# def DFS(x,y,sum):
#     global maxx
#     # print(x,y)
#     # print(sum)
#     # print(res)
#     if x == 6 and y == 6:
#         if maxx > sum:
#             maxx = sum
#             print(sum)
#         return
#
#     # print(x,y)
#     else:
#         for i,j in [[1,0],[0,1],[-1,0],[0,-1]]: # 동 남 서 북
#             if x+i < 0 or y+j < 0 or x+i > 6 or y+j > 6:
#                 continue
#
#             if (res[x+i][y+j] >=sum+1) or (res[x+i][y+j] == 0):
#                 res[x+i][y+j] = sum+1
#                 DFS(x+i,y+j,sum+1)
#
# if __name__ == "__main__":
#     res = [list(map(int,input().split())) for _ in range(7)]
#     maxx = 2147000000
#     ch = [[0]*7 for _ in range(7)]
#     # print(ch)
#     # print(res)
#     DFS(0,0,0)