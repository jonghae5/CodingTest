
'''강의 풀이'''

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = "".join(map(str,stack))
print(res)


# '''오종해 풀이'''
# number, n = map(int,input().split())
# result = [int(i) for i in str(number)]
# final = []
# cnt=0
#
# for i in result:
#     while final and final[-1] < i and cnt < n :
#             final.pop()
#             cnt += 1
#
#     final.append(i)
#
#
#
# final = final[:cnt-n]
# # while cnt < n:
# #     final.pop()
# #     cnt+=1
#
# final_result = "".join(map(str,final))
# print(int(final_result))

