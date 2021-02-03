def solution(n):        
    ls = [0,1,1]
    if n<3:
        return ls[n]
    else:
        for i in range(1,n-1):
            ls.append(ls[i]+ls[i+1])
        
    return ls[n]%1234567
