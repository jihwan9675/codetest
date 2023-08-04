N = int(input())
rock = list(map(int, input().split()))
check = [1] * N

for i in range(1, N):
    f = 0
    for j in range(i):
        if rock[j] < rock[i]:
            f = max(f, check[j])
    check[i] = f+1

print(max(check))
