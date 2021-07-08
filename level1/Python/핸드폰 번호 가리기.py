def solution(phone_number):
    answer = ""
    
    for i in range(len(phone_number)-4):
        answer+="*"
    
    sub=list(answer)+list(phone_number[len(phone_number)-4:])
    
    return ''.join(sub)
