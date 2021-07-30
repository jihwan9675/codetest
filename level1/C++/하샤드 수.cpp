def solution(x):
    sub=list(str(x))
    sum_s=0
    for i in range(len(sub)):
        sum_s+=int(sub[i])
    
    return True if x%sum_s==0 else False
