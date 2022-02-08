
n = int(input())
n_list = list(map(int,input().split()))

'''강의 풀이'''
def digit_sum(x):
    cnt = 10
    result = 0
    for i in str(x):
        result += int(i)

    return result
max = -2147000000

for x in n_list :
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res = x

print(res)

# def digit_sum(x):
#     cnt = 10
#     result = 0
#     while x > 0:
#         ans_want = x % cnt
#         x = x // cnt
#         result += ans_want
#     return result
# for x in n_list :
#     tot = digit_sum(x)
#     if tot>max:
#         max=tot
#         res = x
#
# print(res)

# def digit_sum(x):
#     cnt = 10
#     result = 0
#     while True:
#         ans_want = x % cnt
#         result += ans_want
#         x = x // cnt
#         if x == 0:
#             return result
#
# max = -2147000000
# for idx in range(len(n_list)):
#     value = digit_sum(n_list[idx])
#     if value > max:
#         max = value
#         final_result = n_list[idx]
#
# print(final_result)
