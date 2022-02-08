n_list = [list(map(int,input().split())) for i in range(7)]

# for i in n_list:
#     print(i)

n = 7
cnt = 0
for i in range(n):
    for j in range(2,n-2):
        if (n_list[i][j-2] == n_list[i][j+2]) and (n_list[i][j-1] == n_list[i][j+1]) :
            cnt+=1
        if (n_list[j-2][i] == n_list[j+2][i]) and (n_list[j-1][i] == n_list[j+1][i]) :
            cnt+=1

print(cnt)

# ''' 강의 풀이'''
# board = [list(map(int,input().split())) for _ in range(7)]
# cnt =0
# for i in range(3):
#     for j in range(7):
#         tmp = board[j][i:i+5]
#         if tmp == tmp[::-1]:
#             cnt+=1
#         for k in range(2):
#             if board[i+k][j]!=board[i+5-k-1][j]:
#                 break
#         else:
#             cnt+=1
#
# print(cnt)
