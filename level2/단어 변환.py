visited = []
N = 0
answer = 0

def dfs(word, target, words, cnt):
    global answer
    
    if word == target:
        answer = cnt
        return
    
    for i in range(N):
        other = 0
        for j in range(len(word)):
            if word[j] != words[i][j]:
                other += 1
        if visited[i] != 1 and other == 1:
            visited[i] = 1
            dfs(words[i], target, words, cnt+1)
            visited[i] = 0

        
def solution(begin, target, words):
    global visited, N
    
    N = len(words)
    visited = [0] * N
    dfs(begin, target, words, 0)

    return answer
