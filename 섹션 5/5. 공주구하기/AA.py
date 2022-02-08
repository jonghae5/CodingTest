# import sys
# sys.stdin = open('input.txt','rt')

from collections import deque
'''오종해 풀이'''

n,m = map(int,input().split())
n_list = list(range(1,n+1))
queue = deque(n_list)
cnt = 1
while len(queue)>1 :
    if cnt == m:
        queue.popleft()
        cnt = 1
    else:
        a = queue.popleft()
        queue.append(a)
        cnt += 1
print(queue[0])


# '''강의 풀이'''
#
# n,m = map(int,input().split())
# n_list = list(range(1,n+1))
# dq = deque(n_list)
#
# while dq:
#     for _ in range(m-1):
#         cur = dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq) ==1:
#         print(dq[0])
#         dq.popleft()


