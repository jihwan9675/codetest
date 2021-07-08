def solution(number, hand):
    answer = ''    
    left = 9
    right = 11
    
    for i in range(len(number)):
        number[i]=number[i]-1
        if number[i]==-1:
            number[i]=10
        if number[i] == 0 or number[i] == 3 or number[i] == 6:
            answer+="L"
            left = number[i] 
        elif number[i] == 2 or number[i] == 5 or number[i] == 8:
            answer+="R"
            right = number[i]
        else:
            a=number[i]//3
            b=number[i]%3
            left_a=left//3
            left_b=left%3
            right_a=right//3
            right_b=right%3
            cal_left=abs(a-left_a)+abs(b-left_b)
            cal_right=abs(a-right_a)+abs(b-right_b)
            if cal_left==cal_right:
                if hand=="left":
                    answer+="L"
                    left = number[i]
                else:
                    answer+="R"
                    right = number[i]
            elif cal_left>cal_right:
                answer+="R"
                right = number[i]
            else:
                answer+="L"
                left = number[i]
    return answer
