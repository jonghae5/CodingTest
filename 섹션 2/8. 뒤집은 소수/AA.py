import sys
# sys.stdin = open('input.txt','rt')

n = int(input())
n_list = list(map(int,input().split()))

def reverse(x):
    result = ""
    value = str(x)
    for i in range(1,len(value)+1):
        result += value[-i]
    return int(result)


def isPrime(x):
    cnt=0
    if x==1:
        return False

    for i in range(2,(x//2)+1):
        if x%i == 0:
            return False
    return x


for n_list in n_list:
    tmp = reverse(n_list)
    if isPrime(tmp):
        print(tmp,end=' ')




''' 강의 풀이'''
# def reverse(x):
#     res = 0
#     while x>0:
#         t = x % 10
#         x = x // 10
#         res = res*10 + t
#
#     return res
#
# def isPrime(x):
#     cnt=0
#     if x==1:
#         return False
#
#     for i in range(2,(x//2)+1):
#         if x%i == 0:
#             return False
#     else:
#       return x
#
# for n_list in n_list:
#     tmp = reverse(n_list)
#     if isPrime(tmp):
#         print(tmp,end=' ')