from collections import deque, defaultdict

def solution(x, y, n):
    visited = defaultdict(int)
    check = deque()
    check.append((x, 0))
    answer = []
    
    while len(check) != 0:
        t, cnt = check.popleft()
        if visited[t] > 0:
            continue
        visited[t] = cnt
        
        if t < y:
            check.append((t+n, cnt+1))
            check.append((t*2, cnt+1))
            check.append((t*3, cnt+1))
        elif t>y:
            continue
        elif t==y:
            answer.append(cnt)
            
    answer.sort()
    if len(answer) == 0:
        return -1
    
    return answer[0]
