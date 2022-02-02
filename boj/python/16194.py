#구할 카드의 개수
card_count=int(input())

#카드팩
card_pack = [0] + list(map(int,input().split()))

for i in range(1,card_count+1):
    li = [] #카드 개수에 따른 상황들
    for j in range(i//2+1):
        li.append(card_pack[i-j]+card_pack[j])
    card_pack[i] = min(li)

print(max(card_pack))
