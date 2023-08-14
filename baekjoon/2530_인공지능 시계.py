A, B, C = map(int, input().split())
N = int(input())
C = C + N

B = C//60 + B
C = C%60

A = A + B//60
B = B % 60

A = A % 24

print(A,B,C)
