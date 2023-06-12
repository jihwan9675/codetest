def solution(n, left, right):
    answer = []
    
    # left-right
    
    for i in range(right-left+1):
        row = (i + left) % n + 1
        col =  (i + left) // n + 1
        answer.append(max(row, col))
        
    
    return answer
