from collections import deque

N = int(input())
M = int(input())

graph = [set() for _ in range(N+1)]
check = [0]*(N+1)
check[1] = 1

for i in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)
    

dq = deque(list(graph[1]))

while dq:
    x = dq.popleft()
    if check[x] == 0:
        check[x] = 1
        for p in list(graph[x]):
            dq.append(p)
            
print(sum(check)-1)
