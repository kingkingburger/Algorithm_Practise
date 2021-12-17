input_num = int(input())
num_li = list(map(int,input()))
result = 0
for i in range(input_num):
    result += num_li[i]

print(result)