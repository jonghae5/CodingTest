
'''
결정 알고리즘 매우 중요 !
최소와 최댓값을 알고 있을 때 최적의 수를 구하는 방법
res 중요!
'''
n, m = map(int,(input().split()))
n_list = list(map(int,input().split()))

lt = n_list[0]
rt = sum(n_list)
res=0
while lt<=rt:
    cnt = 0
    bound = 0
    mid = (lt+rt) //2
    for i in n_list:
        bound+=i
        if bound >= mid:
            cnt+=1
            bound = i

    if cnt < m :
        rt = mid -1
    elif cnt >=m and mid >= max(n_list):
        lt = mid +1
        res = mid

print(res)