from collections import deque

def solution(maps):
    N = len(maps); M = len(maps[0])
    
    before_labber = [[False]*M for _ in range(N)]
    after_labber = [[False]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    check = deque()
    
    for i in range(N):
        flag = True
        for j in range(M):
            if maps[i][j] == 'S':
                check.append([i,j,False])
                flag = False
                break
        if flag==False:
            break

    while len(check) != 0:
        x, y, blabber = check.popleft()
        if maps[x][y] == 'L':
            blabber = True
        if maps[x][y] == 'E' and blabber == True:
            return count[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M and maps[nx][ny] != 'X':
                if blabber == True and after_labber[nx][ny] == False:
                    after_labber[nx][ny] = True
                    check.append([nx, ny, blabber])
                    count[nx][ny] = count[x][y] + 1
                elif blabber == False and before_labber[nx][ny] == False:
                    before_labber[nx][ny] = True
                    check.append([nx, ny, blabber])
                    count[nx][ny] = count[x][y] + 1

    return -1
