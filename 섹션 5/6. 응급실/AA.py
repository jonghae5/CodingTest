from collections import deque
'''오종해 풀이'''

n,m = map(int,input().split())
n_list = list(map(int,input().split()))
queue = deque(n_list)

cnt=0
while queue:
    tmp = max(queue)

    if m ==0:
        if queue[0]>=tmp:
            queue.popleft()
            cnt+=1
            break
        else:
            queue.append(queue.popleft())
            m = n-1
    else:
        if queue[0]>=tmp :
            queue.popleft()
            cnt+=1
            n-=1
            m-=1
        else:
            queue.append(queue.popleft())
            m-=1
print(cnt)
'''오종해 풀이2'''
# while queue:
#     tmp = max(queue)
#     if queue[0] >= tmp:
#         queue.popleft()
#         cnt += 1
#         if m == 0:
#             break
#         else:
#             n-=1
#             m-=1
#     else:
#         queue.append(queue.popleft())
#         if m ==0:
#             m= n-1
#         else:
#             m-=1
# print(cnt)

# '''강의 풀이'''
# n,m = map(int,input().split())
# n_list =[(pos, val) for pos, val in enumerate(list(map(int,input().split())))]
# queue = deque(n_list)
# cnt= 0
# while queue:
#     cur = queue.popleft()
#     if any(cur[1] < x[1] for x in queue):
#         queue.append(cur)
#     else:
#         cnt+=1
#         if cur[0] == m:
#             break
#
# print(cnt)





