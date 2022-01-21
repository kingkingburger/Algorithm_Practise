input = int(input())

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

result = list(str(factorial(input)))

answer = 0

for i in range(1, len(result) + 1):
    if(result.pop() == "0"):
        answer += 1
    else:
        print(answer)
        break