from collections import deque

def solution(number, k):
    answer = []
    
    for p in number:
        while k > 0 and len(answer) !=0 and int(answer[-1]) < int(p):
            check = answer.pop()
            k -= 1
        answer.append(p)

    return ''.join(answer[:len(answer)-k])
