
'''
K번째 약수 풀이
'''
import sys

# sys.stdin= open('input.txt','rt')
n,k = map(int, input().split())

'''내가 한 풀이'''
# num = [i for i in range(1,n+1) if n%i ==0]
# if len(num) < k:
#     print(-1)
# else:
#     print(num[k-1])

# for else 구문
''' 강의 풀이'''
cnt = 0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
