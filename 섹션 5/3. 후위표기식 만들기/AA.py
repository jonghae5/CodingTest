# import sys
# sys.stdin = open('input.txt','rt')
# 


'''오종해 풀이'''

problem = input()

stack = []
res = ""

for x in problem:
    if x.isnumeric():
        res+=x
    if x in "(":
        stack.append(x)
    elif x in ["*","/"]:
        while stack and stack[-1] in ["*","/"]:
            res+=stack.pop()
        stack.append(x)
    elif x in ["+","-"]:
        while stack and stack[-1] !="(":
            res+=stack.pop()
        stack.append(x)
    elif x in [")"]:
        while stack and stack[-1] !="(":
            res+=stack.pop()
        stack.pop()

while stack:
    res+=stack.pop()
print(res)