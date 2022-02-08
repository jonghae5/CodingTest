'''
결정 알고리즘 매우 중요 !
최소와 최댓값을 알고 있을 때 최적의 수를 구하는 방법
res 중요!
첫번째 말 배치 후 그 다음 말 최대 거리로 계속 배치
'''
n, m = map(int,(input().split()))
n_list = []
for i in range(n):
    n_list.append(int(input()))

n_list.sort()
lt = n_list[0]
rt = n_list[n-1]

res= 0
while lt <=rt:
    mid = (lt+rt)//2
    cnt = 1
    origin =n_list[0]
    for i in n_list[1:]:
        if (i - origin) >= mid:
            cnt+=1
            origin = i
    if cnt < m:
        rt = mid-1
    elif cnt >=m:
        res = mid
        lt = mid +1


print(res)