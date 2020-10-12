def solution(n, lost, reserve):
    reserve=list(set(reserve)-set(lost))
    lost=list(set(lost)-set(reserve))
    answer = n-len(lost)

    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer+=1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer+=1
    return answer
