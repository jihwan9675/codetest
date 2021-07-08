def solution(answers):
    answer = [0,0,0]
    answer_1=[1,2,3,4,5]
    answer_2=[2,1,2,3,2,4,2,5]
    answer_3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==answer_1[i%5]:
            answer[0]+=1
        if answers[i]==answer_2[i%8]:
            answer[1]+=1
        if answers[i]==answer_3[i%10]:
            answer[2]+=1
    
    if answer[0]==answer[1] & max(answer)==answer[0]:
        if answer[0]==answer[2]:
            return [1,2,3]
        return [1,2]
    elif answer[0]==answer[2] & max(answer)==answer[0]:
        return [1,3]
    elif answer[1]==answer[2] and max(answer)==answer[2]:
        return [2,3]
    
    return [answer.index(max(answer))+1]
