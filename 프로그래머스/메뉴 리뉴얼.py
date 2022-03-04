# from itertools import combinations

# def solution(orders, course):
#     answer = []
#     dict = {}
#     jo = []
#     for i in course:
#         for order in orders:
#             jo.extend(list(combinations(sorted(order), i)))

#     for i in jo:
#         str = ''
#         a = list(i[0])
#         b = list(i[1])
        
#         for j in a: # 모든 조합 돌기
#             if(j in b): # 조합 안에 같은 글자가 있다면
#                 str += j
#                 str = ''.join(sorted(str)) #글자를 오름차순으로 만들고

#                 if(str not in dict): # 딕셔너리에 넣는다.
#                     dict[str] = 1
#                 dict[str] += 1
    
#     sorted(dict.keys()) #key를 기준으로 sort
    
#     for i in course:
#         result = {}
#         test =[]
#         m = 0 # 각 자리수의 최대값
#         for key, value in dict.items():
#             if(len(key) == i):
#                 result[key] = value
        
#         for value in result.values():
#             if(value >= m):
#                 m = value
        
#         for key, value in result.items():
#             if(value >= m):
#                 test.append(key)
        
#         answer.extend(test)
        
#     answer.sort()
#     return answer


from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        dict = {}
        jo = []
        for order in orders:
            jo.extend(list(combinations(sorted(order), i)))
    
        for i in jo:
            str = ''.join(i)
            if str in dict:
                dict[str] += 1
            else:
                dict[str] = 1
                
        for order in dict:
            if dict[order] == max([dict[order] for order in dict]):
                if(dict[order] > 1):
                    answer.append(order)
        
    answer.sort()
    return answer
