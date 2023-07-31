bag, N = map(int, input().split())

golds= []
answer = 0
W = 0

for i in range(N):
    weight, price = map(int, input().split())
    golds.append([weight, price])

golds.sort(key=lambda x:x[1], reverse=True)

for i in range(len(golds)):
    if W < bag:
        if golds[i][0] <= (bag - W):
            W += golds[i][0]
            answer += golds[i][1] * golds[i][0]
        else:
            answer += golds[i][1] * (bag - W)
            break
            
print(answer)
