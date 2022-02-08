# import sys
# sys.stdin = open('input.txt','rt')



'''강의 풀이'''
n = int(input())
n_list = [list(map(int,input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=n_list[i][j]
        sum2+=n_list[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1+=n_list[i][i]
    sum2+=n_list[-1-i][i]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)

'''오종해 풀이'''
# n= int(input())
#
# menu = []
# for _ in range(n):
#     n_list = list(map(int,input().split()))
#     menu.append(n_list)
#
# sum_cro_ri = sum_cro_le = 0
# sum_row = sum_col = 0
# result=[]
# largest = -2147000000
# for i in range(n):
#     sum_row = sum_col = 0
#     sum_cro_ri += menu[i][i]
#     sum_cro_le += menu[n - i - 1][i]
#     for j  in range(n):
#         sum_row += menu[i][j]
#         sum_col += menu[j][i]
#
#     result.append(sum_row)
#     result.append(sum_col)

#
# result.append(sum_cro_ri)
# result.append(sum_cro_le)
#
# for k in result:
#     if k > largest:
#         max = k
#
# print(max)

