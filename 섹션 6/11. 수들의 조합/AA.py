import sys
import itertools as it
# sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
for x in it.combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)

'''순열 만들기 a에서 3개를 뽑아서 만들어라'''
# a = list(range(1,5))
# for x in it.permutations(a,3):
#     print(x)


'''오종해 풀이'''
# # 재귀함수와 스택
# import sys
# # sys.stdin = open("input.txt","r")
#
# def DFS(L,q,sum):
#     global cnt
#     if L == k :
#         if sum % m == 0:
#             cnt+=1
#         return
#     else:
#         for i in range(q,n):
#             p[L] = n_list[i]
#             DFS(L+1,i+1,sum+p[L])
#
#
#
# if __name__ =="__main__":
#     n,k = map(int,input().split())
#     n_list = list(map(int,input().split()))
#     m = int(input())
#     result= []
#     cnt = 0
#     p = [0] * k
#
#     DFS(0,0,0)
#     print(cnt)
