
problem = input()
result = []
bar = 0
# laser = 0
res=0
for x in problem:
    if x == "(":
        bar+=1
    elif result[-1] =="(" and x == ")":
        bar -=1
        # laser +=1
        res+=bar
    elif result[-1] ==")" and x == ")":
        res+=1
        bar -=1
    result.append(x)


print(res)

'''강의 풀이'''
# s = input()
# stack = []
# cnt = 0
# for i in range(len(s)):
#     if s[i] =='(':
#         stack.append(s[i])
#     else:
#         if s[i-1] =='(':
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt+=1
