sub_num=int(input())
l = list(map(int,input().split(" ")))

max_num = max(l)

l = [(int(i)/int(max_num))*100 for i in l]
print(sum(l)/sub_num)