N, M = map(int, input().split())

ls=[0]*N

for i in range(M):
    A, B, C = map(int, input().split())
    for j in range(A-1, B):
        ls[j]=C

for p in ls:
    print(p,end=' ')
