# import sys
# sys.stdin = open('input.txt','rt')

n,m = map(int,input().split())
n_list = list(map(int,input().split()))

'''강의 풀이'''
lt = 0
rt = 1
tot = n_list[0]
cnt = 0
while True:
    if tot < m:
        if rt<n:
            tot+=n_list[rt]
            rt+=1
        else:
            break

    elif tot == m:
        cnt+=1
        tot-=n_list[lt]
        lt+=1
    else:
        tot-=n_list[lt]
        lt+=1
print(cnt)

'''오종해 풀이'''
# n,m = map(int,input().split())
# n_list = list(map(int,input().split()))
# cnt=0
# for i in range(n):
#     ans = 0
#     for j in range(i,n):
#         ans+=n_list[j]
#         if ans == m:
#             cnt+=1
#             break
#         elif ans > m:
#             break
# print(cnt)
#
