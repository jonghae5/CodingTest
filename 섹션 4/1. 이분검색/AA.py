
n, m = map(int,(input().split()))
n_list = list(map(int,input().split()))

n_list.sort(reverse=False)
a = n_list.copy()

lt = 0
rt = n-1
def binary_search(a,m,lt,rt):
    mid = (lt+rt)//2
    if m <a[mid] :
        # print("작습니다.")
        rt = mid-1
        return binary_search(a,m,lt,rt)
    elif m > a[mid]:
        # print("큽니다")
        lt = mid+1
        return binary_search(a,m,lt,rt)
    elif m == a[mid]:
        # print("찾았습니다.")
        return mid+1

result = binary_search(a,m,lt,rt)
print(result)

# ''' 강의 풀이 (중복값이 있는 경우)'''
#
# n, m = map(int,(input().split()))
# n_list = list(map(int,input().split()))
#
# n_list.sort(reverse=False)
# a = n_list.copy()
# print(a)
# lt = 0
# rt = n-1
#
# while lt<=rt:
#     mid = (lt+rt)//2
#     if m < a[mid]:
#         print("작다")
#         rt = mid -1
#     elif m > a[mid]:
#         print("크다")
#         lt = mid +1
#     elif m == a[mid]:
#         print("찾았습니다")
#         print(mid+1)
#         rt = mid -1
#
#

