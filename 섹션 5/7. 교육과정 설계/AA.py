from collections import deque
'''오종해 풀이'''

word = list(input())
n= int(input())

for i in range(n):
    res=""
    queue = deque(input())
    for _ in range(len(queue)):
        if queue[0] not in word:
            queue.popleft()
        else:
            if res and res[-1] == queue[0]:
                queue.popleft()
            elif len(res) <len(word):
                res+=queue.popleft()
            elif len(res) == len(word):
                break
    if res == ''.join(word):
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i + 1))

#
# '''강의 풀이'''
#
# need = input()
# n = int(input())
# for i in range(n):
#     plan = input()
#     dq = deque(need)
#     for x in plan:
#         if x in dq:
#             if x != dq.popleft():
#                 print("#{} NO".format(i + 1))
#                 break
#     else:
#         if len(dq) == 0 :
#             print("#{} YES".format(i + 1))
#         else:
#             print("#{} NO".format(i + 1))
#