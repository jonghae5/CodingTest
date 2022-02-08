# 재귀함수와 스택
import sys
sys.stdin = open("input.txt","r")

'''
위에다 올린 것과 밑에다 올린 것의 차이?
재귀 함수는 스택을 이용하기 때문이다.
함수를 Stack에 다 기록한다. (매개변수, 지역변수, 복귀주소) 이런 묶음들을 Stack Frame 이라고 한다.

'''
def DFS(n):
    if n<1:
        return
    DFS(n-1)
    print(n, end= ' ')

# def DFS(n):
#     if n<1:
#         return
#     print(n)
#     DFS(n-1)
    # if n>0:
    #     print(n)
    #     DFS(n-1)

if __name__ =="__main__":
    n = int(input())
    DFS(n)
