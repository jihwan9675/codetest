def solution(s):
    answer = [0,0]
    
    while True:
        if s == '1':
            break
        for p in s:
            if p == '0':
                answer[1] += 1
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        answer[0] += 1

    return answer
