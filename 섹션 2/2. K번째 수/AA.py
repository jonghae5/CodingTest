import sys
# sys.stdin = open('input.txt','rt')
ans = list()
t = int(input())

for i in range(t):
    n,s,e,k = map(int,input().split())
    number = list(map(int, input().split()))

    result = number[s-1:e]
    result.sort(reverse=False)

    ans.append(result[k-1])

for j in range(t):
    print('#{} {}'.format(j+1,ans[j]))
