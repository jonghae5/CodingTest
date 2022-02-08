import sys
from collections import deque
import itertools as it

def Dsort(lt,rt):
    global arr

    if lt<rt:
        pivot = rt
        pos = lt
        for i in range(lt,rt):
            if arr[i] <= arr[pivot]:
                arr[i],arr[pos] = arr[pos],arr[i]
                pos+=1
        arr[pos], arr[pivot] = arr[pivot],arr[pos]
        print(arr)
        Dsort(lt,pos-1)
        Dsort(pos+1,rt)
    else:
        return




if __name__ =="__main__":

    arr = [23,11,45,36,15,67,33,21]
    print("Before Sort:",arr)
    aaaa=0
    Dsort(0,7)

    print()
    print("After Sort:", arr)