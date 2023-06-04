def solution(k, m, score):
    answer = 0
    
    box_count = int(len(score) / m)
    
    score.sort()

    for i in range(box_count):
        ls = []
        for j in range(m):
            ls.append(score.pop())
        answer += min(ls) * m
        
    
    return answer
