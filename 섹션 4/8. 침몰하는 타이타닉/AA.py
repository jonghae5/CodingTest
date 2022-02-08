
'''그리디 알고리즘'''

n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort(reverse=True)

cnt = 0
while people:
    summ = people[0] + people[-1]
    if len(people) ==1 :
        cnt+=1
        people.pop()
        break
    if summ > m:
        people.pop(0)
        cnt += 1
    elif summ <= m:
        people.pop(0)
        people.pop()
        cnt += 1

print(cnt)
