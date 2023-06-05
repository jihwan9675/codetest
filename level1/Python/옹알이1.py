def solution(babbling):
    answer = 0
    ls_3 = ["aya","woo"]
    ls_2 = ["ye", "ma"]
                
    for p in babbling:
        flag = False
        for s in ls_3:
            if s*2 in p:
                flag = True
        for s in ls_2:
            if s*2 in p:
                flag = True
        if flag:
            continue
        while True:
            if p[:2] in ls_2:
                p = p[2:]
            elif p[:3] in ls_3:
                p = p[3:]
            else:
                break
        if p == '':
            answer +=1
    return answer
