
import sys



def DFS(L,sum):
    global maxx
    if L > n+1:
        return
    if L==n+1:
        if sum > maxx:
            maxx = sum

    else:
        for i in range(L,len(result)):

            DFS(i+result[i][0],sum+result[i][1])
        DFS(L+1,sum)


if __name__ =="__main__":
    n = int(input())
    result = [(0,0)]
    for _ in range(n):
        t,p = map(int,input().split())
        result.append((t,p))
    maxx = -2147000000
    DFS(1,0)
    print(maxx)

#
# '''오종해 풀이'''
# def DFS(L,sum):
#     global maxx, ch
#     if ch[L] == 1:
#         DFS(L+1,sum)
#     if L >n:
#         if sum > maxx:
#             maxx = sum
#         return
#     else:
#         if ch[L] != 1:
#             if result[L][0]>(n-L+1):
#                 DFS(L+1,sum)
#             else:
#                 for i in range(L,result[L][0]+L):
#                     ch[i] = 1
#                 DFS(L+1,sum+result[L][1])
#
#                 for i in range(L,result[L][0]+L):
#                     ch[i] = 0
#                 DFS(L+1,sum)
#
# if __name__ =="__main__":
#     n = int(input())
#     result = [(0,0)]
#     for _ in range(n):
#         t,p = map(int,input().split())
#         result.append((t,p))
#     ch =[0] *(n+2)
#     maxx = -2147000000
#
#
#     DFS(1,0)
#     print(maxx)