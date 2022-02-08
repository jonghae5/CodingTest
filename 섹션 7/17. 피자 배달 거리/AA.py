import sys
from collections import deque
import itertools as it

'''DFS 강의풀이'''


def DFS(L, s):
    global maxxx
    if L == m :
        result = 0
        for hs_x,hs_y in house:
            # print(hs_x,hs_y)
            dist = 2147000000
            for o in ch:
                pz_x = pizza[o][0]
                pz_y = pizza[o][1]
                # print(pz_x, pz_y)
                dist = min(dist,(abs(hs_x-pz_x) + abs(hs_y - pz_y)))
            # print(summ)
            result +=dist

        if maxxx > result:
            maxxx = result

        return

    else:
        # 순열
        for i in range(s,len(pizza)):
            ch[L] = i
            DFS(L+1,i+1)

if __name__ == "__main__":

    maxxx= 2147000000
    n,m = map(int,input().split())
    res = [list(map(int,input().split())) for _ in range(n)]
    house = []
    pizza = []
    ch = [0] * m
    for i in range(n):
        for j in range(n):
            if res[i][j] == 2 :
                pizza.append((i,j))
            elif res[i][j] ==1:
                house.append((i,j))

    DFS(0,0)
    print(maxxx)


'''오종해 풀이 (구현)'''
# n,m = map(int,input().split())
#
# res = [list(map(int,input().split())) for _ in range(n)]
# direct = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북
#
# pizza = []
# house = []
# val = []
# # 1. 피자집 찾기
# for i in range(n):
#     for j in range(n):
#         if res[i][j] == 2:
#             pizza.append((i,j))
#         elif res[i][j] ==1:
#             house.append((i,j))
#
# pizza = list(it.combinations(pizza, m))
#
# maxx = 2147000000
# for pizza in pizza:
#     result = [100] * len(house)
#     for i,j in pizza:
#         for idx,hs in enumerate(house):
#             dist = abs(hs[0]-i) + abs(hs[1]-j)
#             if result[idx] > dist:
#                 result[idx] = dist
#
#     summ = sum(result)
#     if maxx > summ:
#         maxx = summ
#
# print(maxx)


#
# ''' BFS 시간초과'''
# n,m = map(int,input().split())
#
# res = [list(map(int,input().split())) for _ in range(n)]
# direct = [[0,1],[1,0],[0,-1],[-1,0]] # 동 남 서 북
#
# pizza = []
# # 1. 피자집 찾기
# for i in range(n):
#     for j in range(n):
#         if res[i][j] == 2:
#             pizza.append((i,j))
#
# # 2. 피자집 경우의 수 (m개의 피자집)
# pizza = list(it.combinations(pizza, m))
#
# queue = deque()
# maxx = 2147000000
# # 3. BFS
# for k in pizza:
#     ch2 = [[0] * n for _ in range(n)]  # 길이 여부
#     summ = 0
#     for i,j in k:
#         queue.append((i, j))
#         ch1 = [[0] * n for _ in range(n)]  # 방문 여부
#         ch1[i][j] = 1
#         while queue:
#             row,col = queue.popleft()
#             for k,l in direct:
#                 row+=k
#                 col+=l
#
#                 if row<0 or col<0 or row>n-1 or col>n-1:
#                     row-=k
#                     col-=l
#                     continue
#                 if ch1[row][col] == 0:
#                     ch1[row][col] = 1
#                     queue.append((row, col))
#
#                     if res[row][col] == 1:
#                         if ch2[row][col] == 0:
#                             ch2[row][col] = abs(i - row) + abs(j - col)
#                         elif (abs(i-row) + abs(j-col)) < ch2[row][col]:
#                             ch2[row][col] = abs(i-row) + abs(j-col)
#                 row-=k
#                 col-=l
#     for i in range(n):
#         for j in range(n):
#                 summ += ch2[i][j]
#     # print(summ)
#     if maxx > summ:
#         maxx = summ
#     # print(ch2)
#
#
# print(maxx)