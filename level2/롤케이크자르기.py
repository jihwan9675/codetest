def solution(topping):
    answer = 0
    first = dict()
    second = dict()
    
    for i in range(len(topping)):
        if topping[i] not in first:
            first[topping[i]] = 1
        else:
            first[topping[i]] += 1
    
    for i in range(len(topping)):
        if topping[i] not in second:
            second[topping[i]] = 1
        else:
            second[topping[i]] += 1
        first[topping[i]] -= 1
        if first[topping[i]] == 0:
            del first[topping[i]]
        
        if len(first) == len(second):
            answer += 1
    return answer
