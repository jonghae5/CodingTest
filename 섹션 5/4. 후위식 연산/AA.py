
'''오종해 풀이'''

problem = input()

stack = []
res = ""

for x in problem:
    if x.isnumeric():
        stack.append(int(x))
    elif x =="+":
        x1=stack.pop()
        x2=stack.pop()
        stack.append(x2+x1)
    elif x =="-":
        x1=stack.pop()
        x2=stack.pop()
        stack.append(x2-x1)
    elif x =="*":
        x1=stack.pop()
        x2=stack.pop()
        stack.append(x2*x1)
    elif x =="/":
        x1=stack.pop()
        x2=stack.pop()
        stack.append(x2/x1)

print(stack[0])