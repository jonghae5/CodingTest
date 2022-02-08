import sys
# 재귀함수와 스택
def DFS(start,end):
    global ch,res,cnt
    if start == end:
        # print(res)
        cnt+=1
        return
    else: # 0 1 2 3 4
        for idx,val in enumerate(result[start-1]):
            if val ==1 and ch[idx] ==0:
                res.append(idx+1)
                ch[idx] = 1
                DFS(idx+1,n)
                ch[idx] = 0
                res.pop()

if __name__ =="__main__":
    n,m = map(int,input().split())
    result = [[0]*n for _ in range(n)]

    for i in range(m):
        row,col = map(int,input().split())
        result[row-1][col-1] = 1

    ch=[0]*n
    ch[0] = 1
    res = [1]
    cnt = 0
    DFS(1,n)
    print(cnt)

# 출발 도착 가중치
# 행 열 값
# if __name__ =="__main__":
#     n,m = map(int,input().split())
#     n_list = [list(map(int,input().split())) for _ in range(m)]
#
#     result = [[0]*n for _ in range(n)]
#
#     for i in range(m):
#         row = n_list[i][0]
#         col = n_list[i][1]
#         val = n_list[i][2]
#         result[row-1][col-1] = val
#
#     for j in result:
#         for k in j :
#             print(k,end=' ')
#         print()