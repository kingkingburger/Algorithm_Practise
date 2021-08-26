import string
S = list(input())
li = list(string.ascii_lowercase)

result = [-1]*26

for index,value in enumerate(S):
    for j in range(26):
        if(li[j]==value):
            if(result[j]<0):
                result[j] = index   


for i in result:
    print(i, end=' ')
