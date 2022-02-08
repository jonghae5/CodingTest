a = int(input())
a_list = list(map(int,input().split()))
b = int(input())
b_list = list(map(int,input().split()))

result =[]
p1=p2=0

while p1<a and p2<b:
    if a_list[p1] < b_list[p2]:
        result.append(a_list[p1])
        p1+=1
    elif a_list[p1] >= b_list[p2]:
        result.append(b_list[p2])
        p2+=1

if p1<a:
    result=result+a_list[p1:]
if p2<b:
    result=result+b_list[p2:]
#
for result in result:
    print(result, end= ' ')





''' 오종해 풀이'''
# a = int(input())
# a_list = list(map(int,input().split()))
# b = int(input())
# b_list = list(map(int,input().split()))
#
# result =[]
# p1,p2 =0,0
# for i in range(a+b):
#     if (p1<a) and (p2<b) and (a_list[p1] < b_list[p2]) :
#         result.append(a_list[p1])
#         p1+=1
#     elif(p1<a) and (p2<b) and a_list[p1] >= b_list[p2] :
#         result.append(b_list[p2])
#         p2+=1
# if p1<a:
#     result = result + a_list[p1:]
# if p2 < b:
#     result = result + b_list[p2:]
# print(result)

