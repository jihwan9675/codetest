from collections import deque

N, M = map(int, input().split())

visited = [[False]*M for _ in range(N)]
graph = []
answer = 1

for i in range(N):
    graph.append(list(map(int, list(input()))))

    
def dfs():
    global visited, answer, graph
    queue = deque()
    queue.append([0, 0])
    
    dx = [-1, 0, 1 ,0]
    dy = [0, 1 ,0, -1]
    while queue:
        i, j = queue.popleft()
        for q in range(4):
            x = i+dx[q]
            y = j+dy[q]
            if 0<=y<M and 0<=x<N and visited[x][y]==False and graph[x][y] == 1:
                graph[x][y] = graph[i][j] + 1
                queue.append([x, y])

dfs()
print(graph[N-1][M-1])
