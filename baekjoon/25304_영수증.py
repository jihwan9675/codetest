S = int(input())
N = int(input())

answer = 0
for i in range(N):
    A, B = map(int, input().split())
    answer += A*B

if S == answer:
    print('Yes')
else:
    print('No')
