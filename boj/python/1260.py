from collections import deque

N, M ,V = map(int,input().split())

#DFS 메서드 정의
def dfs(graph, v, visited):
    #현제 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현제 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌때 까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for _ in range(N+1)] 
for i in range(M):
    node, link = map(int,input().split())

    graph[node].append(link)
    graph[link].append(node)
    graph[node].sort()
    graph[link].sort()

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * int(N+1)

#정의된 DFS 함수 호출
dfs(graph, V, visited)

visited = [False] * int(N+1)
print()

#정의된 bfs 함수 호출
bfs(graph, V, visited)
