from collections import deque

def solution(s):
    answer = 0
    
    st_count = []
    
    # 01234 12340 23401
    
    for i in range(len(s)):
        text = s[i:len(s)] + s[0:i]
        ls = deque()
        for p in text:
            if p == '[' or p == '{' or p == '(':
                ls.append(p)
            elif p == ']' or p == '}' or p == ')':
                if len(ls) == 0:
                    break
                t = ls.pop()
                if t != '[' and p == ']':
                    break
                elif t != '{' and p == '}':
                    break
                elif t != '(' and p == ')':
                    break
        else:
            if len(ls) == 0:
                answer += 1
                    
                        
    
    return answer
