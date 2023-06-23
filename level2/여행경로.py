visitied = []
answer = []
N = 0
  
    
def dfs(tickets, temp):
    global answer, visitied
    
    if len(temp) == N + 1 and 0 not in visitied:
        answer.append(temp)
        return
    
    for i in range(N):
        if tickets[i][0] == temp[len(temp)-1] and visitied[i] == 0:
            visitied[i] = 1
            dfs(tickets, temp + [tickets[i][1]])
            visitied[i] = 0
    
    
def solution(tickets):
    global visitied, N
    
    N = len(tickets)
    visitied = [0] * N

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visitied[i] = 1
            dfs(tickets, tickets[i])
            visitied[i] = 0

    answer.sort()
    
    return answer[0]
