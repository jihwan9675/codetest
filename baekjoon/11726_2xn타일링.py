T = int(input())

lx = [0] * 1001
lx[0] = 1
lx[1] = 2
for i in range(2, T+1):
    lx[i] = (lx[i-2] + lx[i-1]) % 10007

print(lx[T-1])
