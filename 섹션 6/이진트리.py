# 재귀함수와 스택
import sys
sys.stdin = open("input.txt","r")

'''
위에다 올린 것과 밑에다 올린 것의 차이?
재귀 함수는 스택을 이용하기 때문이다.
함수를 Stack에 다 기록한다. (매개변수, 지역변수, 복귀주소) 이런 묶음들을 Stack Frame 이라고 한다.

'''
def foward_DFS(x,n):
    if x>n:
        return
    else:
        print(x, end=' ')
        foward_DFS(x*2,n) # 왼쪽 노드
        foward_DFS(x*2+1,n) # 오른쪽 노드

def middle_DFS(x,n):
    if x>n:
        return
    else:

        foward_DFS(x*2,n)
        print(x, end=' ')
        foward_DFS(x*2+1,n)

def backward_DFS(x,n):
    if x>n:
        return
    else:
        foward_DFS(x*2,n)
        foward_DFS(x*2+1,n)
        print(x, end=' ')

if __name__ =="__main__":
    n = int(input())
    foward_DFS(1,n)
    print()
    middle_DFS(1,n)
    print()
    backward_DFS(1,n)

