N = int(input())

work = []
move = []


for i in range(N-1):
    workA, workB, moveA, moveB = map(int, input().split())
    work.append([workA, workB])
    move.append([moveA, moveB])
work.append(list(map(int, input().split())))

dpA = [work[0][0]] * N
dpB = [work[0][1]] * N

for i in range(1, N):
    a, b = work[i]
    mA, mB = move[i-1]
    dpA[i] = min(dpA[i-1]+a, dpB[i-1] + mB + a)
    dpB[i] = min(dpA[i-1] + mA + b, dpB[i-1]+b)

print(min(dpA[N-1], dpB[N-1]))
