def solution(s):
    answer = True
    
    li =[]
    for i in s:
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