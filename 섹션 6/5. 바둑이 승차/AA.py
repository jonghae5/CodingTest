
def DFS(v,summ,tsum):
    global maxx
    if (summ+(total-tsum))<maxx or (summ > w):
        return

    if v==num:
        if summ > maxx:
            maxx = summ

    else:
        DFS(v+1,summ+dog[v],tsum+dog[v])
        DFS(v+1,summ,tsum+dog[v])




if __name__ =="__main__":
    w,num = map(int,input().split())
    dog = []
    for i in range(num):
        dog.append(int(input()))
    total = sum(dog)
    maxx = 0
    DFS(0,0,0)
    print(maxx)

