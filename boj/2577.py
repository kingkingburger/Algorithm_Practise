l = [int(input()) for _ in range(3)]
mul = str(l[0] * l[1] * l[2])
for i in range(10):
    print(mul.count(str(i)),end=" ")


#count()는 특정 문자열에서 매개변수로 들어온 값이 몇개 있는지 알려준다.
#아래 코드는 count()매서드를 몰랐을 때 경우입니다.

# result = [0 for _ in range(10)]
# l = [int(input()) for _ in range(3)]
# mul = l[0] * l[1] * l[2]

# numbers = []
# while(mul != 0):
#     numbers.append(mul%10)
#     mul = mul//10

# for i in numbers:
#     result[i] +=1
# for j in result:
#     print(j)