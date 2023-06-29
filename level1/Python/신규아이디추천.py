def solution(new_id):
    answer = ''
    check = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    new_id = new_id.lower()
    temp = ''
    for p in new_id:
        for c in check:
            if p == c:
                temp += c
                
    while temp.find("..") != -1:
        temp = temp.replace('..', '.')
    
    if temp[0] == '.' or temp[-1] == '.':
        if temp[0] == '.':
            temp = temp[1:]
        if len(temp) > 0 and temp[-1] == '.':
            temp = temp[:-1]
        
    
    if temp == '':
        temp = 'a'
    
    if len(temp) > 15:
        if temp[14] == '.':
            temp = temp[:14]
        else:
            temp = temp[:15]
    
    if len(temp) < 3:
        temp = temp + temp[-1] * (3-len(temp))

    return temp
