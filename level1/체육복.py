def solution(n, lost, reserve):
    answer = n-len(lost)
    num=[]
    for i in range(len(lost)):
        if lost[i] in reserve:
            num.append(lost[i])
            answer+=1
    for i in range(len(num)):
        lost.remove(num[i])
        reserve.remove(num[i])
    # check
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer+=1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer+=1

    return answer
