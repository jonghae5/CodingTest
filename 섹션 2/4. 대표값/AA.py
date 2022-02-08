
'''
내 풀이
round > Python 에서는 round_half_even 방식을 채택한다. 4.5 일 경우 짝수로 간다.
5.5 일경우 6으로 간다. >> int(a+0.5)
'''

n = int(input())
students = list(map(int,input().split()))

ans_mean = int((sum(students)/n)+0.5)
result = students[0] - ans_mean

for i in range(1,len(students)):
    compar = students[i] - ans_mean
    if abs(result) > abs(compar):
        result = compar
        result_num = i
    elif abs(result) == abs(compar):
        if result < compar:
            result = compar
            result_num = i

print(ans_mean, (result_num+1))


'''강의 풀이'''
# n = int(input())
# students = list(map(int,input().split()))
# ans_min = 2147000000
# ans_mean = int(round(sum(students)/n,0))
# for idx,x in enumerate(students):
#     tmp = abs(x-ans_mean)
#     if tmp < ans_min:
#         ans_min = tmp
#         score = x
#         res = idx+1
#
#     elif tmp == ans_min:
#         if x>score:
#             res = idx+1
#             score = x
#             ans_min = tmp
#
# print(ans_mean,res)


