def solution(s):
    answer = [-1, ]
    
    for i in range(1, len(s)):
        if s[:i].rfind(s[i]) == -1:
            answer.append(-1)
        else:
            answer.append(len(s[:i])-s[:i].rfind(s[i]))
    
    return answer
