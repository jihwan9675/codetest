def solution(s, n):
    answer = ''
    for i in range(len(s)):
        sub=ord(s[i])+n
        if ord(s[i])==32:
            sub-=n
        elif ord(s[i])<91:
            if sub>90:
                sub-=26
        elif ord(s[i])<123:        
            if sub>122:
                sub-=26
        
        answer+=chr(sub)
    
    return answer
