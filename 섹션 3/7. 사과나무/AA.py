# import sys
# sys.stdin = open('input.txt','rt')

'''오종해 풀이 // 강의랑 같음'''
n = int(input())
n_list = [list(map(int,input().split())) for _ in range(n)]

center = n//2
lt = center # 중심
rt = center+1 # 중심 바로 뒤


result = 0
for i in range(n):
    for j in range(lt,rt):
        result = result+n_list[i][j]
    if i >= center:
        lt +=1
        rt -=1
    else:
        lt-=1
        rt+=1

print(result)

