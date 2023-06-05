def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        flag = True
        for spell in target:
            short = 100
            for k in keymap:
                if spell in k:
                    if short > k.find(spell):
                        short = k.find(spell) + 1
            if short == 100:
                short = -1
                flag = False
            count += short
        if flag == False:
            answer.append(-1)
        else:
            answer.append(count)
                        
    return answer
