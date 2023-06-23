from itertools import permutations

def solution(k, dungeons):
    answer = 0
    ls= [i for i in range(len(dungeons))]
    pmt = permutations(ls, len(dungeons))
    
    for p in pmt:
        maxi = 0
        power = k
        for i in p:
            if dungeons[i][0] <= power:
                power -= dungeons[i][1]
                maxi += 1
            else:
                break
        if maxi > answer:
            answer = maxi
        
    return answer

