from itertools import combinations #모든 경우의 수를 찾아줌

from collections import defaultdict
from turtle import st 
#defaultdict()는 딕셔너리를 만드는 dict클래스의 서브클래스이다.
# 작동하는 방식은 거의 동일한데, defaultdict()는 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리값의 초깃값으로 지정할 수 있다.
# 숫자, 리스트, 셋등으로 초기화 할 수 있

def solution(info, query):
                
    answer = []
    infos = defaultdict(list)

    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])

        for n in range(5):
            combi = list(combinations(range(4),n)) # [0,1,2,3] , [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]...
            for c in combi: # [0,1,2,3] , [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]...
                t_c = conditions.copy() # ['java', 'backend', 'junior', 'chicken'] #
                for v in c: # 지원 자들의 조건을 만들 수 있는 모든 경우의 수는 key
                    t_c[v] = '-' # 0,1,2,3 ~ 01, 02, 03 ~ 123 ~ 0123 ~ 
                infos['/'.join(t_c)].append(score) 
    
    for item in infos:
        infos[item].sort()


    for q in query:
        q = q.replace('and','').split() # ['java', 'backend', 'junior', 'pizza', '100']
        conditions = '/'.join(q[:-1]) # java/backend/junior/pizza
        score = int(q[-1]) # 100

        if conditions in list(infos): # java/backend/junior/pizza

            data = infos[conditions]
            if(len(data) > 0):
                start, end = 0, len(data)
                while start != end and start != len(data):
                
                    if(data[(start + end) // 2] ) >= score: # 왼쪽 탐색
                        end = (start + end)  // 2
                    else:
                        start = (start + end) // 2 + 1  # 오른쪽 탐색
                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])