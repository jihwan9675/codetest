def solution(k, score):
    answer = [score[0]]
    
    sc = [score[0]]
    
    for i in range(1, len(score)):
        if len(sc) < k:
            sc.append(score[i])
        elif min(sc) < score[i]:
            sc.append(score[i])
            sc.sort(reverse=True)
            sc.pop()
        answer.append(min(sc))
    
    return answer
