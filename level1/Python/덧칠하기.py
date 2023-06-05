def solution(n, m, section):
    answer = 1
    
    check = m +section[0] 
    
    for i in range(1, len(section)):
        if section[i] >= check:
            check = section[i] + m
            answer +=1
        
    
    return answer 
