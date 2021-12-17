
while(True):
    try:
        input_num1, input_num2 = map(int, input().split(" "))
        print("%d" %(input_num1+input_num2) )
    except EOFError:
        break