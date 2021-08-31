word = input()
count = 0
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for j in alphabet:
    if(j in word):
        word = word.replace(j, ",")

count = word.count(",")
word = word.replace(",","")
print(count + len(word))


