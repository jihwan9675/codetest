N = int(input())

#2^(N-1)
answer = 2

for i in range(1,N+1):
    answer += 2**(i-1)

print(answer**2)
