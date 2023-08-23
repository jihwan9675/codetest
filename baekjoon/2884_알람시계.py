H, M = map(int, input().split())

M = M-45
if M <0:
    M=M+60
    H=H-1
    if H<0:
        H+=24
        
print(H,M)
