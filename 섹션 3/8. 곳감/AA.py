

'''강의 풀이'''

n = int(input())
n_list = [list(map(int,input().split())) for i in range(n)]
m = int(input())

for i in range(m):
    row, direct, number = map(int, input().split())
    if direct ==0:
        for _ in range(number):
            n_list[row-1].append(n_list[row-1].pop(0))
    else:
        for _ in range(number):
            n_list[row-1].insert(0,n_list[row-1].pop())

center = n//2
s = 0
e = n-1
result = 0
for i in range(n):
    for j in range(s,e+1):
        result+= n_list[i][j]
    if i<center:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(result)
#
#
#
# '''오종해 풀이 / 잘못된 풀이 순환이 안됨.. '''
# n = int(input())
# n_list = [list(map(int,input().split())) for i in range(n)]
# m = int(input())
#
# for i in range(m):
#     row, direct, number = map(int, input().split())
#     if direct == 0:
#         n_list[row-1] = n_list[row-1][number:] + n_list[row-1][:number]
#     elif direct:
#         n_list[row-1] = n_list[row-1][n-number:] + n_list[row-1][:n-number]
#
# center = n//2
# s = 0
# e = n-1
# result = 0
# for i in range(n):
#     for j in range(s,e+1):
#         result += n_list[i][j]
#     if i<center:
#         s +=1
#         e -=1
#     else:
#         s -=1
#         e +=1
#
# print(result)
#
