test_case = int(input())

for i in range(test_case):
    x,y = map(int, input().split())

    distance = y-x
    count = 0 # 이동 횟수
    move = 1 # 이동 가능 거리
    move_count = 0 #이동 거리 합
    while(move_count < distance):
        count +=1
        move_count += move
        if count % 2 ==0:
            move +=1
    print(count)
        


