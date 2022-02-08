n,m = map(int,input().split())
ans = dict()
result = list()


for i in range(1,n+1):
    for j in range(1,m+1):
        res = i+j

        if res in ans:
            ans[res] += 1
        else:
            ans[res] = 1

value = sorted(list(ans.values()),reverse=True)[0]

for key in ans:
    if ans[key] == value:
        result.append(key)
        print(key, end=' ')

'''
강의풀이
'''
# max = -2147000000
# n,m = map(int,input().split())
# cnt = [0]*(n+m+3) # 넉넉히 잡음 3은 의미없음
#
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         cnt[i+j]+=1
#
# for i in range(n+m+1):
#     if cnt[i] > max:
#         max = cnt[i]
#
# for i in range(n+m+1):
#     if cnt[i] == max:
#         print(i, end=' ')
#
