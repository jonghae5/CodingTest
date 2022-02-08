
'''그리디 알고리즘'''

'''
강의 풀이
회의가 끝나는 시점부터 정렬을 한다.
끝 시간을 기준으로 하면 남은 시간이 비든 말든 최댓값을 반환한다.
'''

n = int(input())
n_list = [tuple(map(int,input().split())) for _ in range(n)]

n_list.sort(key= lambda x: (x[1],x[0])) # 뒷 순위가 0번 start
et = 0
cnt = 0

for s, e in n_list:
    if s>= et:
        cnt+=1
        et = e
print(cnt)


'''오종해 풀이 (잘못)'''

# n = int(input())
# n_list = [list(map(int,input().split())) for _ in range(n)]
# max = -2147000000
# for i in range(n):
#     cnt = 1
#     start = n_list[i][0]
#     end = n_list[i][1]
#
#     for j in range(i+1,n):
#         if n_list[j][0] >= end:
#             cnt+=1
#             start = n_list[j][0]
#             end = n_list[j][1]
#
#     if cnt > max :
#         max = cnt
# print(max)

