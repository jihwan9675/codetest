def solution(a, b):
    answer = 0
    if b<a:
        sub=a
        a=b
        b=sub
    for i in range(a,b+1):
        answer+=i
    return answer
