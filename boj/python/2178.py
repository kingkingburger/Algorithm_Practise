from collections import deque
import sys
sys.setrecursionlimit(10**6)

w, h  = map(int,input().split())

#2차원 배열 만들기
graph = []
for i in range(w):
    graph.append(list(map(int,input())))

def check_round(x,y):
    if(x <= -1 or x >= w or y <= -1 or y >= h): #범위 밖으로 나가면
        return False
    else:
        return True

#BFS 메서드 정의
def bfs(result_x,result_y):
    #큐 구현을 위해 deque 사용
    queue = deque([[0,0,0]])
    #현재 노드를 방문 처리
    graph[0][0] = 0
    #큐가 빌때 까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        x = v[0]
        y = v[1]
        count = v[2]

        #목적지에 오면 동작
        if(x == result_x-1 and y == result_y-1):
            print(count+1)
            break

        if (check_round(x+1,y) ): #하
            if(graph[x+1][y] == 1):
                queue.append([x+1, y ,count+1])
                graph[x+1][y] = 0

        if (check_round(x,y+1)): #우
            if(graph[x][y+1] == 1 ):
                queue.append([x, y+1 ,count+1])
                graph[x][y+1] = 0

        if (check_round(x-1,y) ): #상
            if(graph[x-1][y] == 1):
                queue.append([x-1, y ,count+1])
                graph[x-1][y] = 0

        if (check_round(x,y-1)): # 좌
            if(graph[x][y-1] == 1 ):
                queue.append([x, y-1 ,count+1])
                graph[x][y-1] = 0

#정의된 bFS 함수 호출
bfs(w,h)

