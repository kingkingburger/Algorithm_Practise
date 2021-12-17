input_string = input().upper()
unique_word = list(set(input_string))

li = []
for i in unique_word:
    word = input_string.count(i)
    li.append(word)

# 중복되는 것들이 1개 이상이라면
if(li.count(max(li))>1):
    print("?")
else:
    print(li)
    print(unique_word)
    max_index = li.index(max(li))
    print(unique_word[max_index])