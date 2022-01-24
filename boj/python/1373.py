binary = list(map(int,input()))
result = ""


for i in range(0,len(binary),3):
    if(len(binary) <3):
        binary = [0,0] + binary

    x = binary.pop() * 1
    y = binary.pop() * 2
    z = binary.pop() * 4
    result = str(x+y+z) + result
print(result)