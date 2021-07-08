def solution(s):
    answer = ""
    answer_1 = ""
    
    for i in range(len(s)):
        if s[i].islower():
            answer+=""+s[i]
        else:
            answer_1+=""+s[i]
    
    return "".join(sorted(answer, reverse=True)+sorted(answer_1,reverse=True))
