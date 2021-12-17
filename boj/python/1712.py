a,b,c = map(int,input().split())

result =0 
#손익분기점 = 고정가격 / (제품 당 가격 - 가변비용)
if((c-b) <= 0):
    result = -1
else:   
    result = (a/(c-b)) + 1
    
print(int(result))