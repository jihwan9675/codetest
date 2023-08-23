H, M = map(int, input().split())
N = int(input())

M = M+N

if M>=60:
    H+=M//60
    M=M%60
    H = H%24
        
print(H,M)
