def solution(a, b):
    n, m= a, b
    gc=1
    while True:
        if min(n,m)==n:
            n, m=m,n
        if n%m==0:
            gc=m
            break
        n, m = m, n-m 
    
    return [gc,a*b/gc]
