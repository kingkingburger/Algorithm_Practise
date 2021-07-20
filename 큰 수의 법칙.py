n, m ,k = list(map(int,input().split()))
arr = list(map(int,input().split()))

count =0
result = 0
s_max_num = 0

for _ in range(m):
    count += 1
    max_num = max(arr)
    max_index = arr.index(max_num)
    s_max_num = max_num

    if((count % k)== 0):
        arr[max_index] = 0
        max_num = max(arr)

    result += max_num
    arr[max_index] = s_max_num
    

print(result)

