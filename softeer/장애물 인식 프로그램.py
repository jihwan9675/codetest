from collections import deque


N = int(input())
pane = []
visited = []
answer = []
dx = [-1, 0 , 1, 0]
dy = [0 , 1, 0, -1]

def bfs(i, j):
    global visited
    count = 0
    path = deque()
    path.append([i, j])

    while path:
        x, y = path.popleft()
        
        if visited[x][y] == 0 and pane[x][y] == 1:
            count += 1
            visited[x][y] = 1
            for q in range(4):
                if 0<= x+dx[q] < N and 0<=y+dy[q]<N:
                    path.append([x+dx[q], y+dy[q]])
    
    return count

# 방문 리스트, 지도 입력 받기
for i in range(N):
    pane.append(list(map(int, list(input())))) # 지도
    visited.append([0] * N) # 방문

# Process
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and pane[i][j] == 1:
            count = bfs(i, j) # row, column, count
            answer.append(count)

answer.sort() # 오름차순 정렬

# Output
print(len(answer)) # 갯수
for count in answer:
    print(count) # 카운트 수
