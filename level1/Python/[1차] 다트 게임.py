import re
def solution(dartResult):
    answer = re.findall("\d+", dartResult)
    for i in range(3):
        dartResult=dartResult.replace(answer[i]," ",1)
        answer[i]=int(answer[i])
    check_digit = -1
    for i in range(len(dartResult)):
        if dartResult[i]==" ":
            check_digit+=1
        elif dartResult[i].isalpha():    
            if dartResult[i]=="D": 
                answer[check_digit]=answer[check_digit]**2
            elif dartResult[i]=="T": 
                answer[check_digit]=answer[check_digit]**3
        else:
            if dartResult[i]=="*":
                answer[check_digit]*=2
                if check_digit!=0:
                    answer[check_digit-1]*=2
            elif dartResult[i]=="#":
                answer[check_digit]*=-1
            
                
    return sum(answer)
