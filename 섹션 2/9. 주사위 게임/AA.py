
n = int(input())


n_list=[]
final = []
for i in range(n):
    data = list(map(int,input().split()))
    n_list.append(data)


'''오종해 풀이'''
for i in range(n):
    result = n_list[i][0]
    res_cnt = 1

    for j in range(1,len(n_list[i])):
        if res_cnt == 2:
            if result == n_list[i][j]:
                res_cnt+=1
        else:
            if result == n_list[i][j]:
                res_cnt+=1
            elif result < n_list[i][j]:
                result = n_list[i][j]

    if res_cnt == 3:
        final.append(10000 + result * 1000)
    elif res_cnt == 2:
        final.append(1000 + result * 100)
    else:
        final.append(result * 100)
print(sorted(final,reverse=True)[0])


'''
강의 풀이
가장 좋은 것을 if로 사용
'''
# res = 0
# for i in range(n):
#     tmp = input().split()
#     tmp.sort()
#
#     a,b,c = map(int, tmp)
#     if a==b and b==c:
#         money = 10000 + a * 1000
#     elif a==b or a==c:
#         money = 1000 + a* 100
#     elif b==c:
#         money = 1000 + b * 100
#     else:
#         money = 100 * c
#     if money > res:
#         res= money
# print(res)


