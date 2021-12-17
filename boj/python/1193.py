result = int(input())
count = 0
x=0
y=0

while(result > count):
    
    result =result - count
    floor = count + 1
    count +=1


#짝수면
if(floor%2 == 0):
    x = result
    y = (floor+1) - result
else:
    x = (floor+1) - result
    y = result 
print(str(x)+"/"+str(y))