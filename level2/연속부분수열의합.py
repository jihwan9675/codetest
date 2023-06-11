def solution(elements):
    answer = 0
    
    Set_answer = set()
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            if j+i+1 < len(elements):
                Set_answer.add(sum(elements[j:j+i+1]))
            else:
                Set_answer.add(sum(elements[j:len(elements)] + elements[0:j+i+1-len(elements)]))
    
    return len(Set_answer)
