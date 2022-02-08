import sys
from collections import deque

n = int(input())
res = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
ch[n//2][n//2] = 1

queue = deque()
queue.append((n//2,n//2))
direct = [[0,-1],[1,0],[0,1],[-1,0]] # 서 남 동 북

result = res[n//2][n//2]
L =0

while queue:
    if L == n//2 :
        print(result)
        break
    for k in range(len(queue)):
        i,j = queue.popleft()
        for row,col in direct:

            i += row
            j += col
            if ch[i][j] == 0 :
                ch[i][j] = 1
                result += res[i][j]
                queue.append((i,j))
            i -= row
            j -= col
    L+=1


# '''오종해 풀이'''
# n = int(input())
# res = [list(map(int,input().split())) for _ in range(n)]
# ch = [[0]*n for _ in range(n)]
# ch[0][0] = 1
#
# queue = deque()
# queue.append((0,0))
# direct = [[0,-1],[1,0],[0,1],[-1,0]] # 서 남 동 북
#
# result = 0
#
# while queue:
#     i,j = queue.popleft()
#     for row,col in direct:
#
#         i += row
#         j += col
#         if (i < 0) or (j < 0) or (i > n-1) or (j > n-1):
#             i -= row
#             j -= col
#             continue
#
#         elif ch[i][j] == 0 :
#             ch[i][j]=1
#             queue.append((i,j))
#             if i <= n//2 and j in list(range(n//2-i,n//2+i+1)):
#                 result += res[i][j]
#             if i> n//2 and j in list(range(i-n//2,n-(i-n//2))):
#                 result += res[i][j]
#         i -= row
#         j -= col
#
# print(result)
