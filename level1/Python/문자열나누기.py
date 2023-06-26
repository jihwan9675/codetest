def solution(s):
    answer = 0

    same = 0
    other = 0

    for i in range(len(s)):
        if same == 0:
            cs = s[i]
        if s[i] == cs:
            same += 1
        else:
            other += 1
        if same == other:
            answer += 1
            same = 0
            other = 0
    if same !=0 or other !=0:
        answer += 1
        
    return answer
