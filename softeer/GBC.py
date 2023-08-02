N, M = map(int, input().split())

building = [0] * 100
interval = [[0,0]]
Vs = [[0,0]]

for i in range(N):
    x, y = map(int, input().split())
    interval.append([x+interval[-1][0], y])

for i in range(M):
    x, y = map(int, input().split())
    Vs.append([x + Vs[-1][0], y])
for x in range(1, len(Vs)):
    for i in range(Vs[x-1][0], Vs[x][0]):
        building[i] += Vs[x][1]

for x in range(1, len(interval)):
    for i in range(interval[x-1][0], interval[x][0]):
        building[i] -= interval[x][1]

answer = max(building)
if answer <0:
    print(0)
else:
    print(max(building))
