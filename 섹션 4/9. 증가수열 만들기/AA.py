'''강의 풀이'''
n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
res = ""
tmp = []
last = 0
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt+=1
        else:
            rt-=1

    tmp.clear()
print(len(res))
print(res)


'''그리디 알고리즘'''


# n = int(input())
# n_list = list(map(int,input().split()))
#
# result =[]
# tmp = 0
# while n_list:
#
#     s = n_list[0]
#     e = n_list[-1]
#     if len(n_list) == 1 and s > tmp:
#         tmp = s
#         n_list.pop()
#         result.append("L")
#     if (s > tmp) and (e > tmp):
#         if (s < e):
#             tmp = s
#             n_list.pop(0)
#             result.append("L")
#         else:
#             tmp = e
#             n_list.pop()
#             result.append("R")
#     elif (s > tmp) or (e > tmp):
#         if (s < e):
#             tmp = e
#             n_list.pop()
#             result.append("R")
#         else:
#             tmp = s
#             n_list.pop(0)
#             result.append("L")
#     else:
#         break
# print(len(result))
# print("".join(result))
