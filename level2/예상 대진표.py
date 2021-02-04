def solution(n,a,b):
    answer=1
    
    for i in range(n):
        if a+b==3:
            break
        if a//2*2!=a:
            a+=1
        if b//2*2!=b:
            b+=1
        if a==b:
            break
        a=a//2
        b=b//2
        answer+=1
    return answer
