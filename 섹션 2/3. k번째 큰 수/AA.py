import sys
# sys.stdin = open('input.txt','rt')


'''
강의 풀이
'''
n,k = map(int,input().split())
number = list(map(int,input().split()))

res = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(number[i]+number[j]+number[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])



'''오종해 풀이'''
# n,k = map(int,input().split())
# number = list(map(int,input().split()))
#
# number.sort(reverse=True)
#
# ans = list()
# cnt=0
# for i in range(n-2):
#     for j in range(1,n-1):
#         for l in range(2,n):
#             result = number[i]+number[j]+number[l]
#             ans.append(result)
#             cnt+=1
#             if cnt == k:
#                 break
#         if cnt == k:
#             break
#     if cnt == k:
#         break
#
# print(ans[k-1])