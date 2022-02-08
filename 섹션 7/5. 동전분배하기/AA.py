
import sys

def DFS(L):
    global minn,result

    if L ==n:
        if minn <= (max(result) - min(result)):
            return

        for i in range(3):
            for j in range(i+1,3):
                if result[i] == result[j]:
                    return
        if minn > (max(result) - min(result)):
            minn = (max(result) - min(result))

    else:
        for i in range(3):
            result[i] += res[L]
            DFS(L+1)
            result[i] -= res[L]


# N개의 동전을 3명에게 나누어 주려고 한다.
# 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록
if __name__ =="__main__":
    n = int(input())
    res = []
    for _ in range(n):
        res.append(int(input()))
    result=[0] * 3
    minn = 2147000000
    DFS(0)
    print(minn)


'''강의 풀이'''
#
# def DFS(L):
#     global minn,result
#
#     if L ==n:
#         if minn <= (max(result) - min(result)):
#             return
#         elif minn > (max(result) - min(result)):
#             tmp = set()
#             for x in result:
#                 tmp.add(x)
#             if len(tmp) ==3:
#                 minn = (max(result) - min(result))
#
#
#     else:
#         for i in range(3):
#             result[i] += res[L]
#             DFS(L+1)
#             result[i] -= res[L]
#
#
# # N개의 동전을 3명에게 나누어 주려고 한다.
# # 총액이 가장 큰 사람과 가장 작은 사람의 차가 최소가 되도록
# if __name__ =="__main__":
#     n = int(input())
#     res = []
#     for _ in range(n):
#         res.append(int(input()))
#     result=[0] * 3
#     minn = 2147000000
#     DFS(0)
#     print(minn)