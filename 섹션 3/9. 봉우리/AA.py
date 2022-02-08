
'''오종해 풀이'''
n = int(input())
n_list = [[0]*(n+2) for _ in range(n+2)]

for i in range(1,n+1):
    n_list[i][1:n+1] = list(map(int,input().split()))


# print(n_list)
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        # 좌
        if n_list[i][j]>n_list[i][j-1]:
            # 위
            if n_list[i][j]>n_list[i-1][j]:
                # 오른쪽
                if n_list[i][j] > n_list[i][j+1]:
                    # 아래
                    if n_list[i][j] > n_list[i+1][j]:
                        cnt+=1

print(cnt)

#
#
# '''강의 풀이'''
#
# n = int(input())
# n_list = [list(map(int,input().split())) for i in range(n)]
# n_list.insert(0,[0]*n)
# n_list.append([0]*n)
#
# dx = [-1,0,1,0] # 행
# dy = [0,1,0,-1] # 열
# # 위 오른쪽 아래 밑
# cnt=0
# for x in n_list:
#     x.insert(0,0)
#     x.append(0)
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if all(n_list[i][j]> n_list[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt+=1
#
# print(cnt)
