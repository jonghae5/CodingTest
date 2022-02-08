
'''그리디 알고리즘'''
'''
오종해 풀이 / 강의랑 동일
'''

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())

maxx = n_list[0]
minn = n_list[n-1]
cnt=1
result = []
n_list.sort(reverse=True)
for i in range(m):
    n_list[0] -=1
    n_list[n-1] +=1
    if (n_list[0] < n_list[1]) or (n_list[n-2] < n_list[n-1]) :
        n_list.sort(reverse=True)

print(n_list[0] - n_list[n-1])
