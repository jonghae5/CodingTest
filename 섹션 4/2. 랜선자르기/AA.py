# import sys
# sys.stdin = open('input.txt','rt')
'''
결정 알고리즘 매우 중요 !
최소와 최댓값을 알고 있을 때 최적의 수를 구하는 방법
'''
n, m = map(int,(input().split()))
n_list = [int(input()) for _ in range(n)]

lt = 1
rt = max(n_list)
res = 0

while lt<=rt:
    mid = (lt + rt) // 2
    cnt = 0
    for i in n_list:
        cnt += (i//mid)
    if cnt  < m :
        rt = mid -1
    elif cnt >=m :
        lt = mid +1
        res = mid

print(res)

