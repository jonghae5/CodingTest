
import sys


def DFS(L):
    global word,cnt
    if L == len(n):
        cnt+=1
        print(word)
    else:
        for i in range(1,3):
            if i ==2 and L+i > len(n):
                return
            elif int(n[L:L+i]) == 0:
                return
            elif int(n[L:L+i]) <= 25 :
                word += res[int(n[L:L+i])]
                DFS(L+i)
                word = word[:-1]

    pass

# 65 97 chr / ord
# 65 ~ 90 A ~Z
# res = [0] * 65
if __name__ =="__main__":
    n = input()
    word=""
    cnt=0
    res=[None]
    for i in range(26):
        res.append(chr(65+i))

    DFS(0)
    print(cnt)



# '''강의 풀이'''
# def DFS(L,P):
#     global cnt
#     if L== n:
#         cnt+=1
#         for j in range(P):
#             print(chr(64+res[j]),end='')
#         print()
#     else:
#         for i in range(1,27):
#             if code[L]==i:
#                 res[P]=i
#                 DFS(L+1,P+1)
#             elif i>=10 and code[L]==i//10 and code[L+1] == i%10:
#                 res[P] = i
#                 DFS(L+2,P+1)
#
#
#
# if __name__ == "__main__":
#     code = list(map(int,input()))
#     n = len(code)
#     code.insert(n,-1)
#     res = [0]*(n+3)
#     cnt = 0
#     DFS(0,0)
#     print(cnt)