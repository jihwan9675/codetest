def solution(s):
    answer = ''
    check=0
    for i in range(len(s)):
        if ord(s[i])==32:
            check=1
            answer+=s[i]
        elif check%2==0:
            answer+=s[i].upper()
        elif check%2==1:
            answer+=s[i].lower()
        check+=1
    return answer
