num = input()
if(int(num)<10):
    num='0'+num
    
act_num = list(num) # ['2', '6']
count=0

while(True):
    count += 1
    result = int(act_num[0]) + int(act_num[1])# 2+6 = 8
    result= list(str(result))
    try:
        new_num = act_num[1] + result[1]
    except IndexError:
        new_num = act_num[1] + result[0]

    act_num = new_num
    if(new_num == num):
        break
print(count)

#또다른 답 10의자리와 1의자리로 만드는 법
#n=26
#print((n//10 + n%10)%10 +(n%10)*10)