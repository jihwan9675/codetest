def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        temp = 0
        for q in p:
            for i in range(len(name)):
                if name[i] == q:
                    temp += yearning[i]
                    break
        answer.append(temp)
    
    return answer
