'''오종해 풀이'''
n_list = [list(map(int,input().split())) for i in range(9)]

result_row = set()
result_col = set()
result_rect = set()

# 행

for i in range(9):
    for j in range(9):
        result_row.add(n_list[i][j])
    if len(result_row)!=9:
        print("NO")
        break
    result_row = set()
else:
    for i in range(9):
        for j in range(9):
            result_col.add(n_list[j][i])
        if len(result_col) != 9:
            print("NO")
            break
        result_row = set()
    else:
        for i in range(9):
            for j in range((i//3 *3), (i//3 *3) +3): # 행
                for k in range((i % 3) * 3, (i % 3) * 3 + 3): # 열
                    result_rect.add(n_list[j][k])
            if len(result_rect)!=9:
                print("NO")
                break
            result_rect=set()
        else:
            print("YES")


# '''강의 풀이'''
# n_list = [list(map(int,input().split())) for i in range(9)]
# def check(n_list):
#     for i in range(9):
#         ch1 = [0] * 10
#         ch2 = [0] * 10
#         for j in range(9):
#             ch1[n_list[i][j]]=1
#             ch2[n_list[j][i]]=1
#         if sum(ch1) != 9 or sum(ch2) != 9:
#             return False
# 
#     for i in range(3):
#         for j in range(3):
#             ch3=[0]*10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[n_list[i*3+k][j*3+s]] = 1
#                 if sum(ch3)!=9:
#                     return False
#     return True
# 
# if check(n_list):
#     print("YES")
# else:
#     print("NO")