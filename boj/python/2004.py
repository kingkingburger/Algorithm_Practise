n,m = map(int, input().split())

def count_5(x):
    count = 0
    while(x !=0):
        x = x//5 #몫은 개수 이다.
        count += x
    return count

def count_2(x):
    count = 0
    while(x !=0):
        x = x//2 #몫은 개수 이다.
        count += x
    return count

result_5=count_5(n) - count_5(m) - count_5(n-m)
result_2=count_2(n) - count_2(m) - count_2(n-m)
print(count_5(n) , count_5(m) , count_5(n-m))
print(count_2(n) , count_2(m) , count_2(n-m))
print(min(result_2,result_5))
