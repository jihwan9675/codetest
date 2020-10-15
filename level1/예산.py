def solution(d, budget):
    answer = 0
    for i in range(len(d)):
        if budget-min(d)>=0:
            answer+=1
            budget-=min(d)
            d.remove(min(d))
    return answer
