
import sys

def DFS(L,sum):
    global cnt

    if sum > t:
        return
    if L==k:
        if sum == t :
            cnt+=1

        return
    else:
        for i in range(n[L]+1):
                DFS(L+1,sum+p[L]*i)

if __name__ =="__main__":
    t = int(input())
    k = int(input())
    p = [] # 금액
    n = [] # 개수

    for _ in range(k):
        a,b = map(int,input().split())
        p.append(a)
        n.append(b)

    cnt = 0 # 방법 가지 수
    DFS(0,0)
    print(cnt)
