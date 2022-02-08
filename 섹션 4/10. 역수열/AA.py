# import sys
# sys.stdin = open('input.txt','rt')


'''강의 풀이'''
''' 앞의 빈자리만 보는 문제이다.'''
# n = int(input())
# a = list(map(int,input().split()))
# seq = [0] * n
# for i in range(n):
#     for j in range(n):
#         if a[i] ==0 and seq[j] ==0 :
#             seq[j]=i+1
#             break
#         elif seq[j] ==0:
#             a[i]-=1
#
# for x in seq:
#     print(x, end=' ')

'''오종해 풀이'''
n =int(input())
n_list = list(map(int,input().split()))

count = [False]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if count[j] == False:
            cnt+=1
        if cnt == (n_list[i] +1):
            count[j] = i+1
            break

for i in count:
    print(i, end= ' ')

