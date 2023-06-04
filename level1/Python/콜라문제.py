def solution(a, b, n):
    answer = 0
    total = n
    while True:
        if total>=a:
            answer += int((total/a))*b
            total = total%a + int((total/a))*b
        else:
            break
    
    return answer
