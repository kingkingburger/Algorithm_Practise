import sys
sys.setrecursionlimit(10**6)

c = [] # dfs 한 사이클 돌 때 나오는 수
r = [] # 나오는 수를 오름차 순으로 
def dfs(x,y,count):

    #주어진 범위를 벗어나면 종료
    if(x <= -1 or x >= n or y <= -1 or y >= n):
        return False

    if(graph[x][y] == 0):
        return False

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    if(graph[x][y] == 1):
        graph[x][y] = 0

        count += 1 #하나의 사이클의 호출 횟수 
        
        dfs(x-1,y,count)   # 상
        dfs(x,y-1,count)   #왼쪽
        dfs(x,y+1,count)   #오른쪽
        dfs(x+1,y,count)   #아래
        
        c.append(count)
    
        return True
    
n = int(input())

#2차원 배열 만들기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
result = 0

#정의된 DFS 함수 호출
for i in range(n):
    for j in range(n):
        if(dfs(i,j,0) == True): # 한 사이클이 끝남
            result += 1
            r.append(len(c))
            c.clear()

print(result)

r.sort()
for p in r:
    print(p)