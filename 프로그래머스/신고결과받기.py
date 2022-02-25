# def solution(id_list, report, k):
#     result={x : 0 for x in id_list} #신고당한 횟수
#     answer = [0]* len(id_list)

#     for r in set(report):
#         result[r.split()[1]] += 1
    
#     for r in set(report):
#         if result[r.split()[1]] >= k:
            #answer[id_list.index(r.split()[0])] += 1
#     return answer
# 다른사람의 풀이

def solution(id_list, report, k):
    result=[[] for _ in range(len(id_list))] #신고당한 횟수
    answer = [0]* len(id_list)
    stop_list = [0]* len(id_list)

    for user in report: # 신고 목록
        reporter = user.split()[0]
        reported = user.split()[1]
        
        index = id_list.index(reporter)
        if(reported not in result[index]):
            result[index].extend([reported])
        
    #신고 처리 대상
    for j in (result):
        for q in j:
            stop_list[id_list.index(q)] += 1
                
    for i in range(len(id_list)):
        for q in result[i]:
            if(stop_list[id_list.index(q)] >= k): #제제 대상이라면
                answer[i] += 1
            
            
    return answer