# import sys
# sys.stdin = open('input.txt','rt')



''' 강의 풀이'''

card = list(range(21)) # 0 ~ 21
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        card[s+i],card[e-i] = card[e-i],card[s+i]

card.pop(0) # 0번 인덱스 없앰
for k in card:
    print(k,end=' ')


'''
오종해 풀이
'''
# card = [i for i in range(1,21)]
# for i in range(10):
#     batch = list(map(int,input().split()))
#     start = batch[0] -1
#     end = batch[1] -1
#
#     card_fo = card[:start]
#     card_mi = card[start:end+1]
#     card_ba = card[end+1:]
#
#     for j in range(len(card_mi)//2):
#         card_mi[j],card_mi[-1-j] = card_mi[-1-j],card_mi[j]

#
#     card = card_fo + card_mi + card_ba
#
# for card in card:
#     print(card,end=' ')


