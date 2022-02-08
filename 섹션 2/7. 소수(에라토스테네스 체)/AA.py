import sys
n = int(input())
cnt = [0] * (n+1)
result = []
for i in range(2,n+1):
    if cnt[i]==0:
        cnt[i]+=1
        result.append(i)
        for j in range(i*2,n+1,i):
            cnt[j] = -1


print(len(result))

# '''강의 풀이'''
# n = int(input())
# ch = [0] * (n+1)
# cnt = 0
# for i in range(2,n+1):
#     if ch[i]==0:
#         cnt+=1
#         for j in range(i,n+1,i):
#             ch[j]=1
#
# print(cnt)