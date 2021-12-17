test_case = int(input())

for _ in range(test_case):
    
    k = int(input())
    n = int(input())
    f0 = [x+1 for x in range(14)]
    for i in range(k):
        for j in range(1,n):
            f0[j] += f0[j-1]

    print(f0[n-1])
    