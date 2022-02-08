import sys
def DFS(L,sum):
    global cnt

    if L > n:
        if ch[sum] == 1:
            return
        if sum <0:
            return
        else:
            ch[sum] = 1
            cnt+=1
        return
    else:
        DFS(L+1,sum+n_list[L])
        DFS(L+1,sum-n_list[L])
        DFS(L+1,sum)

if __name__ =="__main__":
    n = int(input())
    n_list =  list(map(int,input().split()))
    n_list = [0] + n_list
    m = sum(n_list)
    ch = [0] * (m+1)
    # 사용 유무, + - 사용안하거나  3 개
    cnt = 0
    DFS(1,0)
    print(m-cnt+1)