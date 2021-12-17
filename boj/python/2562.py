input_num = []
for i in range(9):
    input_num.append(int(input()))

print(max(input_num))
print(input_num.index(max(input_num))+1)