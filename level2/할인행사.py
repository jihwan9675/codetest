from collections import deque

def solution(want, number, discount):
    answer = 0
    
    check = [0 for _ in range(len(want))]
    
    for j in range(9):
        if discount[j] in want:
            check[want.index(discount[j])] += 1
    
    for i in range(len(discount)-9):
        if discount[i+9] in want:
            check[want.index(discount[i+9])] += 1
        for j in range(len(check)):
            if number[j] > check[j]:
                break
        else:
            answer += 1
            
        if discount[i] in want:
            check[want.index(discount[i])] -= 1
        
            
    
    return answer 
