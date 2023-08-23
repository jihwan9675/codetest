N, M = map(int, input().split())

ls=[p for p in range(1, N+1)]

for i in range(M):
    A, B = map(int, input().split())
    ls[A-1], ls[B-1] = ls[B-1], ls[A-1]

for p in ls:
    print(p,end=' ')
