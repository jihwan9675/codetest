T = int(input())

def combination(i, j):
    c = 1
    for n in range(i, j+1):
        c *= n
    return c

for i in range(T):
    N, M = map(int, input().split())
    print(int(combination(M-N+1, M) / combination(1, N)))
