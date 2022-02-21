import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

#DFS 메서드 정의
def dfs(v):
    #현재 노드를 방문 처리
    visited[v] = True
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

N, M  = map(int,input().split())

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for _ in range(N+1)] 

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False for _ in range(N+1)]

#dfs가 끝날 때 카운트
count = 0

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

#정의된 DFS 함수 호출
for j in range(1,N+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
