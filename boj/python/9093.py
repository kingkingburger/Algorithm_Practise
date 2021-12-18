test_case = int(input())

while(test_case):
    list = []
    sentence = input().split()
    for i in sentence:
        for j in range(1, len(i)+1):
            print(i[-j],end='')
        print(end=' ')

    test_case -= 1
