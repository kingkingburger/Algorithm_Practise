num = int(input())
t = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

n = str(num)
length = len(n) - 1

result = 0

for i in range(1, length + 1):
    result += 9 * t[i-1] * i

result += (num - t[length] + 1) * len(n)

print(result)
