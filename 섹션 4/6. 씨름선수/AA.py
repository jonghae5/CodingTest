
'''그리디 알고리즘'''
'''
오종해 풀이 / 강의 풀이
'''
n_list = []
n = int(input())
for _ in range(n):
    h, w = map(int,input().split())
    n_list.append((h,w))

n_list = sorted(n_list,key = lambda x : x[0], reverse=True)

max = 0
cnt = 0
for i in range(n):
    if n_list[i][1] > max:
        max = n_list[i][1]
        cnt+=1
print(cnt)