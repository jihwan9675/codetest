def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        if food[i] > 1:
            answer += str(i) * int(food[i]/2)
    
    answer += '0'
    
    for i in range(len(answer)-2, -1, -1):
        answer += str(answer[i])
    
            
    return answer
