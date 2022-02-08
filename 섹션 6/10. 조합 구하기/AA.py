# 재귀함수와 스택
import sys
# sys.stdin = open("input.txt","r")
def DFS(L,q):
    global cnt
    if q > (n+1):
        return
    if L == m :
        for x in p:
            print(x,end=" ")
        cnt+=1
        print()
        return
    else:
        for i in range(q,n+1):
            p[L] = i
            DFS(L+1,i+1)

if __name__ =="__main__":
    n,m = map(int,input().split())
    cnt = 0
    p = [0] * m
    DFS(0,1)
    print(cnt)

''' 강의풀이1'''
# def DFS(L,q):
#     global cnt
#     if q > n:
#         return
#     if L == m :
#         for x in p:
#             print(x,end=" ")
#         cnt+=1
#         print()
#         return
#     else:
#         for i in range(q,n+1):
#             if ch[i] ==0:
#                 ch[i] = 1
#                 p[L] = i
#                 DFS(L+1,i)
#                 ch[i] = 0
#
# if __name__ =="__main__":
#     n,m = map(int,input().split())
#     cnt = 0
#     p = [0] * m
#     ch = [0] * (n+1)
#     DFS(0,1)
#     print(cnt)


'''오종해 풀이'''
#
#
# def DFS(L):
#     global cnt
#     if L == m :
#         if set(p) not in q :
#             q.append(set(p))
#             for x in p:
#                 print(x,end=" ")
#             cnt+=1
#             print()
#         return
#     else:
#         for i in range(1,n+1):
#             if (ch[i] ==0) and (i not in q):
#                 ch[i] = 1
#                 p[L] = i
#                 DFS(L+1)
#                 ch[i] = 0
#
#
# if __name__ =="__main__":
#     n,m = map(int,input().split())
#     cnt = 0
#     q = []
#     p = [0] * m
#     ch = [0] * (n+1)
#     DFS(0)
#     print(cnt)




