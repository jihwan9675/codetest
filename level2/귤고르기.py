def solution(k, tangerine):
    answer = 0
    
    #tangerine.sort()
    
    _set = list(set(tangerine))
    count = []
    dic= dict()
    
    for p in tangerine:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    ls = sorted(dic.values(), reverse = True)
    
    sum = 0
    for i in range(len(ls)):
        if sum < k:
            sum += ls[i]
            answer += 1
    
    return answer 
