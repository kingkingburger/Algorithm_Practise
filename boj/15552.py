import sys
test_case = int(input())

for i in range(test_case):
    input_num_1, input_num_2  = map(int,sys.stdin.readline().split(" "))
    if(input_num_1 > 1000 or input_num_2 > 1000):
        break
    print(input_num_1 + input_num_2)