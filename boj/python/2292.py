input_num = int(input())
count = 0

result = input_num - 1
while(True):
    result =result - (6 * count)
    if(result <=0):
        count +=1
        break
    count +=1
print(count)