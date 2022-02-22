import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):

    #주어진 범위를 벗어나면 종료
    if(x <= -1 or x >= h or y <= -1 or y >= w):
        return False

    if(graph[x][y] == 0):
        return False

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    if(graph[x][y] == 1):
        graph[x][y] = 0
        dfs(x-1,y-1) #왼쪽 위 대각선
        dfs(x-1,y)   # 상
        dfs(x-1,y+1) #오른쪽 위 대각선

        dfs(x,y-1)   #왼쪽
        dfs(x,y+1)   #오른쪽

        dfs(x+1,y-1) #왼쪽 아래 대각선
        dfs(x+1,y)   #아래
        dfs(x+1,y+1) #오른쪽 아래 대각선
        return True



while(True):
    w, h  = map(int,input().split())

    if(w==0 and h==0):
        break

    #2차원 배열 만들기
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))

    
    result = 0

    #정의된 DFS 함수 호출
    for i in range(h):
        for j in range(w):
            if(dfs(i,j) == True):
                result += 1
    print(result)
