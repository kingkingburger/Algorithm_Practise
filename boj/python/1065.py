input_num = int(input())

count = 0
for i in range(1,input_num+1):
    
    if(i > 100):
        a = (i//100)
        b = ((i%100)//10)
        c = ((i%10)//1)
        #print(a, b,c, c-b, b-a)
        if((a-b) == (b-c)):
            count +=1
    elif(i < 100):
        count +=1
print(count)