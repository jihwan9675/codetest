K, P, N = map(int, input().split())

temp = 1
for i in range(N):
    temp = (temp * P) % 1000000007

print(K*temp% 1000000007)
