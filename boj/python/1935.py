import string
test_num = int(input())

calculation = input()
english = list(string.ascii_uppercase)

stack = []
#후위 표기식에 숫자 넣기
for i in range(test_num):
    word = input()
    #replace는 변환된 문자열을 반환함
    calculation = calculation.replace(english[i], word, calculation.count(english[i]))

calculation = list(calculation)

for i in calculation:
    #문자가 숫자이면
    if(i.isalnum()):
        stack.append(i)
    else:
        n2 = float(stack.pop())
        n1 = float(stack.pop())
        if (i == '+'):
            stack.append(n1 + n2)
        elif(i == '-'):
            stack.append(n1 - n2)
        elif(i == '*'):
            stack.append(n1 * n2)
        elif(i == '/'):
            stack.append(n1 / n2)
        # stack.append(result)

print(format(stack[0], ".2f"))
