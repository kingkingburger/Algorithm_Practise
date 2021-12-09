n, m = map(int, input().split())
# m = 깊이
base = []
visited = [False for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m +1):
        base.append(j)
    base.append(i)

print(base)
def dfs(base, v, visited):
    for i in range(n):
        visited[i] = True
        print(v+1, end=' ')
    
    for i in base:
        if not visited[i]:
            dfs(base, i, visited)

dfs(base, 2, visited)
