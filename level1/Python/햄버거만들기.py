from collections import deque
    
def solution(ingredient):
    answer = 0
    
    burger = deque()
    
    for p in ingredient:
        if p == 1:
            if len(burger) > 0 and  burger[-1][0] == 1 and burger[-1][1] == 1 and burger[-1][2] == 1:
                burger.pop()
                answer += 1
            else:
                burger.append([1, 0, 0])
        elif p == 2 and len(burger) > 0:
            if burger[-1][2] == 0:
                burger[-1][1] += 1
            else:
                burger[-1][1] += 2
        elif p == 3 and len(burger) > 0:
            if burger[-1][1] == 1:
                burger[-1][2] += 1
            else:
                burger[-1][2] += 2
    return answer
