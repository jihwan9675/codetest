def solution(number, limit, power):
    answer = 0
    ls = [1] * number
    
    for i in range(2, number+1):
        for j in range(i, number+1, i):
            ls[j-1] += 1
    
    for i in range(number):
        if ls[i]  > limit:
            ls[i] = power
    
    return sum(ls)
