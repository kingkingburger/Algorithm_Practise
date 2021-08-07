test_case = int(input())

for i in range(test_case):
    input_num_1, input_num_2  = map(int,input().split(" "))
    print("Case #"+str(i+1)+": " +str(input_num_1+input_num_2))