answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer, visited
    
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if k-dungeons[i][0] >= 0 and k-dungeons[i][1] >= 0 and visited[i] != 1:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global N, visited
    
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    
    return answer
