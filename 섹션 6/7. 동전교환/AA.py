# 재귀함수와 스택


'''강의 풀이'''
# 그리디 알고리즘이 최고인데 굳이 DFS..?
def DFS(ch,problem):
    global maxx, ch1
    result = sum(ch)
    if problem < 0:
        return
    if maxx< result :
        return
    if ch1 == ch:
        return
    elif problem == 0:
        if maxx > result:
            maxx = result
            ch1 = ch.copy()
    else:
        for i in range(n):
            ch[i] += 1
            DFS(ch,problem-n_list[i])
            ch[i] -=1

if __name__ =="__main__":
    n = int(input())
    n_list = list(map(int,input().split()))
    problem = int(input())
    maxx = 2147000000
    ch1=[]
    n_list.sort(reverse=True)
    ch = [0] * (n+1)
    DFS(ch, problem)

    print(maxx)
    # result = [(i,n_list[i]) for i in range(len(n_list))]
