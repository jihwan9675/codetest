from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    check = deque()
    i, j = 0, 0
    check.append([i, j])
    
    dx = [-1, 0 ,1, 0]
    dy = [0, 1 ,0, -1]
    
    while len(check) != 0:
        x, y = check.popleft()
        for k in range(4):
            i = x + dx[k]
            j = y + dy[k]

            if 0<=i<N and 0<=j<M and visited[i][j] == False and maps[i][j] != 0:
                visited[i][j] = True
                maps[i][j] = maps[x][y] + 1
                check.append([i,j])
                
    if maps[N-1][M-1] == 1:
        return -1
    
    return maps[N-1][M-1]
