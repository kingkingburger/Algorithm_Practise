def check(str):
    
    li =[]
    for i in str:
        if(i == '('):
            li.append(i)
        else:
            if(len(li) == 0):
                return False
            li.pop()
            
    if(len(li) == 0):
        return True
    else:
        return False
            
def solution(p):
    answer = ''
    
    left = 0
    right = 0
    
    u = ""
    v = ""
    
    if(len(p) == 0):
        return answer
    
    for value in range(len(p)+1): 
        if(p[value] =='('):
            left += 1
        elif(p[value] == ')'):
            right += 1
        
        if(left != 0 and left == right):
            u = p[0:value+1]
            v = p[value+1:]
            break
            
    if(check(u)):
        answer += u
        answer += solution(v)
        
    else:
        answer += '('
        answer += solution(v)
        answer += ')'


        for q in range(1,len(u)-1):
            if(p[q] == '('):
                answer += ')'
            if(p[q] == ')'):
                answer += '('

        
    return answer