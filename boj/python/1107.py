import sys
input = sys.stdin.readline

channal = int(input())
error_buttons_count = int(input())
e_buttons = list(map(int,input().split()))


min_count = abs(100 - channal)

#고장나지 않은 수로 만들 수 있는 모든 수열
for num in range(1000001): # 1 ~ 1,000,000까지
    #숫자들 중에 특정 숫자가 포함하는지 
    #만약 고장난 버튼이 있다면

    num = str(num)

    for i in range(len(num)):# 4자리면 i는 3이 마지막
        if(int(num[i]) in e_buttons): # 고장난 버튼 판별
            break
        
        elif(i == len(num)-1): # 고장안난 버튼으로 만들 수 있는 채널
            min_count = min( min_count , abs(int(num) - channal)+ len(num) )

print(min_count)

                