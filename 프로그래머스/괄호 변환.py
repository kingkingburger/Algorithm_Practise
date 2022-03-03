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
    
    for value in range(len(p)): # 몇번 째 인덱스에서 귵형잡힌 괄호가 나오는지
        if(p[value] =='('):
            left += 1
        elif(p[value] == ')'):
            right += 1

        if(left != 0 and left == right):
            u = p[0:value+1]
            v = p[value+1:]
            print("u:",u,"v",v)
            break
            
    if(check(u)):
        answer += u
        answer += solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for q in range(1,len(u)):
            if(q == '('):
                answer += ')'
            if(q == ')'):
                answer += '('
    
    return answer

solution("(()())()")
solution("()))((()")