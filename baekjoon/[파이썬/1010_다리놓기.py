N = int(input())
ls = []
answer = [N] * N

for i in range(N):
    q, p = map(int, input().split())
    ls.append([q, p])
    
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if ls[i][0] >= ls[j][0] or ls[i][1] >= ls[j][1]:
            answer[i] -= 1

for i in range(N):
    if i == N-1:
        print(answer[i])
    else:
        print(answer[i], end=' ')
