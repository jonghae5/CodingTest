'''오종해 풀이'''
def DFS(v):

    if v > n:
        list1 = 0
        list2 = 0
        for i in range(n):
            if ch[i] == 1:
                list1+=n_list[i]
            else:
                list2+=n_list[i]
        if (list1 ==0) or (list2 ==0):
            return

        elif list1 == list2:
            ch[-1] = "YES"
        return

    else:
        ch[v-1] = 1
        DFS(v+1)
        ch[v-1] = 0
        DFS(v+1)

if __name__ =="__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    ch = [0] * (n+1)
    ch[-1]= "NO"
    DFS(1)
    print(ch[-1])



# '''강의 풀이'''
#
#
# def DFS(L,sum):
#     if sum > total//2:
#         return
#     elif L == n:
#         if (total - sum) == sum:
#             print("YES")
#             sys.exit(0)
#         return
#
#     else:
#         DFS(L+1,sum+n_list[L])
#         DFS(L+1,sum)
#
#
# if __name__ =="__main__":
#     n = int(input())
#     n_list = list(map(int, input().split()))
#     total = sum(n_list)
#     DFS(0,0) # 인덱스 번호(레벨), 누적하는 합
#     print("NO")