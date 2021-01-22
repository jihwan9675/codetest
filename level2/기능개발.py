import math
def solution(progresses, speeds):
    answer = []
    ls = []
    for i in range(len(progresses)):
        ls.append(math.ceil((100-progresses[i])/speeds[i]))
    print(ls)
    sub = ls[0]
    sub1 = 1
    for i in range(1,len(ls)):
        if sub<ls[i]:
            sub=ls[i]      
            answer.append(sub1)
            sub1= 1
        else:
            sub1+=1
    answer.append(sub1)
    return answer
