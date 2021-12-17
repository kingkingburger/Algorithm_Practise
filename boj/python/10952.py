while(True):
    input_num1, input_num2 = map(int, input().split(" "))
    if((input_num1 == 0 and input_num2 == 0)):
        break
    print("%d" %(input_num1+input_num2) )