def pibo(i):
    if i <= 1:
        return i
    
    return pibo(i-1) + pibo(i-2)
T = int(input())
print(pibo(T))
