N, M = map(int, input().split())

ls = list(map(int, input().split()))
mx = sum(ls[:M])
check = mx
for i in range(M, N):
    check = check - ls[i-M] + ls[i]
    if mx < check:
        mx = check

print(mx)
