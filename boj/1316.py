count = int(input())
new_word = ""
result = 0

for _ in range(count):
    not_group = 0
    word = input()
    for i in range(len(word)-1):
        if(word[i] != word[i+1]):#서로 다른 문자가 오면
            new_word = word[i+1:] # 새로운 문자열을 만든다.
            #남은 글자중에 현재 글자가 있다면
            #그룹 단어가 아니다
            if(new_word.count(word[i]) > 0):
                not_group = 1
    if(not not_group):
        result +=1

print(result)