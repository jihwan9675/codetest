def solution(arr):
    answer = []
    
    for p in arr:
        if p % 2 == 1 and p < 50:
            answer.append(p*2)
        elif p % 2 == 0 and p >=50:
            answer.append(p/2)
        else:
            answer.append(p)
            
    return answer
