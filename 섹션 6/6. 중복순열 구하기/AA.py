
'''강의 풀이'''

def DFS(v,l):
    global result
    if l==m:
        print(" ".join(str(ch[i]) for i in range(len(ch)-1)))
        result+=1
        return
    else:
        for i in range(1,n+1):
            ch[l]=i
            DFS(i,l+1)

if __name__ =="__main__":
    n,m = map(int,input().split())
    ch = [0]*(m+1)
    result= 0
    DFS(0,0)
    print(result)