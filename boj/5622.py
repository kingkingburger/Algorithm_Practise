import string
alphabet = string.ascii_uppercase
count = 0

word = input().upper()
for i in word:
    if(i in alphabet[:3]):
        count += 3
    elif(i in alphabet[3:6]):
        count += 4
    elif(i in alphabet[6:9]):
        count += 5
    elif(i in alphabet[9:12]):
        count += 6
    elif(i in alphabet[12:15]):
        count += 7
    elif(i in alphabet[15:19]):
        count += 8
    elif(i in alphabet[19:22]):
        count += 9
    elif(i in alphabet[22:26]):
        count += 10
print(count)