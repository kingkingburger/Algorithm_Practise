n,k = map(int,input().split())
coin=[]
count = 0

#코인 종류 받기
for i in range(n):
    coin.append(int(input()))

while(coin):# 받은 코인의 종류의 숫자만큼
    #코인의 종류
    count_kind = coin.pop()#리스트의 오른쪽 코인을 뽑으면서 시작

    if(k // count_kind  >= 0):#코인이 n의 배수라면
        count += k//count_kind #몫 저장
        k = k%count_kind #나머지는 다른 코인과 비교

print(count)