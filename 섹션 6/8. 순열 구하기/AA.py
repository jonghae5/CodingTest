
def DFS(L):
    global cnt
    if L == m:
        for x in p:
            print(x,end=" ")
        cnt+=1
        print()
        return
    else:
        for i in range(1,n+1):
            if ch[i] ==0:
                ch[i] = 1
                p[L] = i
                DFS(L+1)
                ch[i] = 0



if __name__ =="__main__":
    n,m = map(int,input().split())
    cnt = 0
    p = [0] * m
    ch = [0] * (n+1)
    DFS(0)
    print(cnt)



