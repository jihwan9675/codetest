def solution(clothes):
    answer = 1
    
    ls = dict()
    
    for p in clothes:
        if p[1] not in ls:
            ls[p[1]] = [p[0]]
        else:
            ls[p[1]] += [p[0]]
            
    for p in ls:
        answer *= len(ls[p]) + 1
            
    
    return answer -1
