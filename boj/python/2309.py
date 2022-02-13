result = []
for i in range(9):
    result.append(int(input()))

sum_a = sum(result)
Flag= False
for i in range(9):
    for j in range(i+1,9):
        if(100 == sum_a -(result[i] + result[j])):
            result[i] = 0
            result[j] = 0
            result.sort()
            Flag = True
            break
    if(Flag):
        break    
for k in range(2, len(result)):
    print(result[k])

