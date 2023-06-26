from collections import deque

def solution(priorities, location):
    answer = 0
    
    ls = [[i, p] for i, p in enumerate(priorities)]
    que = deque(ls)

    while len(que) > 0:
        temp = que.popleft()
        if len(que) == 0:
            if location == temp[0]:
                answer+= 1
            break
        elif temp[1] < max(que, key=lambda x:x[1])[1]:
            que.append(temp)
        else:
            answer += 1
            if location == temp[0]:
                break
            
    return answer



